# Licensed under the MIT License.
# Copyright (c) 2025-2035. All rights reserved by Hanhan Wu.
# Permission is hereby granted to view this code for evaluation purposes only.
# You may not reuse, copy, modify, merge, publish, distribute, sublicense,
# or exploit this code without Hanhan Wu's EXPLICIT written permission.

import asyncio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from pydantic import BaseModel, Field
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import matplotlib.image as mpimg
from statistics import mode

from langchain_google_vertexai import ChatVertexAI
from langchain.chat_models import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser

import warnings
warnings.filterwarnings('ignore')


# ------------------------------------ GENERAL ------------------------------------ #
def calculate_confidence(row):
    scores = [row['rr_auto_score_gpt5'], row['rr_auto_score_gemini'], row['rr_auto_score_mistral']]
    mode_score = mode(scores)[0] # Get the mode of the scores
    confidence = scores.count(mode_score) / len(scores)  # Proportion of voters agreeing with the mode
    return confidence


def plot_answer_usefulness_scores(df, score_columns):
    """
    Plots a line chart comparing answer usefulness scores across multiple columns.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the answer usefulness score columns.
        score_columns (list): List of column names to compare.
    """
    # Define the possible scores
    scores = [0, 0.2, 0.4, 0.8, 1.0]
    
    # Initialize the plot
    plt.figure(figsize=(10, 6))
    
    # Loop through each column and calculate percentages
    for col in score_columns:
        percentages = df[col].value_counts(normalize=True).reindex(scores, fill_value=0) * 100
        avg_score = df[col].mean()
        plt.plot(scores, percentages, marker='o', label=f"{col} (avg: {avg_score:.2f})")

        # Annotate each point with the percentage value
        for x, y in zip(scores, percentages):
            plt.text(x, y + 0.5, f"{y:.2f}%", ha='center', fontsize=9)
    
    # Add labels, title, and legend
    plt.xlabel('Answer Usefulness Score')
    plt.ylabel('Percentage (%)')
    plt.title('Comparison of Answer Usefulness Scores')
    plt.xticks(scores)
    plt.legend(title="Answer Columns")
    plt.grid(True)
    
    # Show the plot
    plt.show()
# ------------------------------------ GENERAL ------------------------------------ #


# ------------------------------------ RETRIEVAL RELEVANCY ------------------------------------ #
class RetrievalRelevancy(BaseModel):
    score: int = Field(description="""Score with:
                                        1: if the RETRIEVED CONTENT has nothing to do with the USER QUERY
                                        2: if the RETRIEVED CONTENT seems relevant to USER QUERY but doesn't answer the USER QUERY
                                        3: if the RETRIEVED CONTENT is relevant to USER QUERY and can directly answer the USER QUERY
                        """)
    reasoning: str = Field(description="Reasoning for the given score.")


async def evaluate_retrieval_relevancy_async(llm, user_query, retrieved_content, rr_prompt_template):
    base_parser = PydanticOutputParser(pydantic_object=RetrievalRelevancy)
    output_parser = OutputFixingParser.from_llm(parser=base_parser, llm=llm)
    prompt = PromptTemplate(
        template=rr_prompt_template,
        input_variables=["user_query", "retrieved_content"],
        partial_variables={"format_instructions": output_parser.get_format_instructions()},
    )
    chain = prompt | llm | output_parser
    result = await chain.ainvoke({"user_query": user_query, "retrieved_content": retrieved_content})
    return result


async def process_record_async(llm, record, rr_prompt_template):
    query = record['query']
    retrieved_content = record['retrieved_content']
    eval_result = await evaluate_retrieval_relevancy_async(llm, query, retrieved_content, rr_prompt_template)
    rr_score = eval_result.score
    rr_reasoning = eval_result.reasoning

    record['rr_auto_score'] = rr_score
    record['rr_reasoning'] = rr_reasoning
    return record


async def get_retrieval_relevancy_output_async(input_df, llm_model_str, rr_prompt_template, model='vertexai'):
    input_records = input_df.to_dict(orient='records')
    if model == 'openai':
        llm = ChatOpenAI(temperature=1, model_name=llm_model_str)  # temperature ahs to be 1 here
    elif model == 'mistral':
        llm = ChatMistralAI(temperature=0, model_name=llm_model_str)
    else:
        llm = ChatVertexAI(temperature=0, model=llm_model_str)
    tasks = [process_record_async(llm, record, rr_prompt_template) for record in input_records]
    output_lst = await asyncio.gather(*tasks)
    output_df = pd.DataFrame(output_lst)
    return output_df
# ------------------------------------ RETRIEVAL RELEVANCY ------------------------------------ #


# ------------------------------------ ANSWER USEFULNESS ------------------------------------ #
class AnswerUsefulness(BaseModel):
    score: float = Field(description="""Score with:
                                        1.0: Exceptional answer that excels in all criteria
                                        0.8: Excellent answer with minor room for improvement
                                        0.6: Good answer that adequately addresses the USER QUERY
                                        0.4: Fair answer with significant room for improvement
                                        0.2: Poor answer that barely addresses the USER QUERY
                                        0.0: Completely inadequate or irrelevant answer
                        """)
    reasoning: str = Field(description="Reasoning for the given score.")


async def evaluate_answer_usefulness_async(llm, user_query, ai_answer, referenced_answer, au_prompt_template):
    base_parser = PydanticOutputParser(pydantic_object=AnswerUsefulness)
    output_parser = OutputFixingParser.from_llm(parser=base_parser, llm=llm)
    prompt = PromptTemplate(
        template=au_prompt_template,
        input_variables=["user_query", "ai_answer", "referenced_answer"],
        partial_variables={"format_instructions": output_parser.get_format_instructions()},
    )
    chain = prompt | llm | output_parser
    result = await chain.ainvoke({
        "user_query": user_query,
        "ai_answer": ai_answer,
        "referenced_answer": referenced_answer
    })
    return result


async def process_answer_usefulness_record_async(llm, record, au_prompt_template):
    eval_result = await evaluate_answer_usefulness_async(
        llm,
        record['query'],
        record['answer'],
        record['referenced_answer'],
        au_prompt_template
    )
    record['answer_usefulness_score'] = eval_result.score
    record['au_reasoning'] = eval_result.reasoning
    return record


async def get_answer_usefulness_output_async(input_df, llm_model_str, au_prompt_template, model='vertexai'):
    input_records = input_df.to_dict(orient='records')
    if model == 'openai':
        llm = ChatOpenAI(temperature=1, model_name=llm_model_str)  # temperature ahs to be 1 here
    elif model == 'mistral':
        llm = ChatMistralAI(temperature=0, model_name=llm_model_str)
    else:
        llm = ChatVertexAI(temperature=0, model=llm_model_str)
    tasks = [process_answer_usefulness_record_async(llm, record, au_prompt_template) for record in input_records]
    output_lst = await asyncio.gather(*tasks)
    output_df = pd.DataFrame(output_lst)
    return output_df
# ------------------------------------ ANSWER USEFULNESS ------------------------------------ #