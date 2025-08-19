# Licensed under the MIT License.
# Copyright (c) 2025-2035. All rights reserved by Hanhan Wu.
# Permission is hereby granted to view this code for evaluation purposes only.
# You may not reuse, copy, modify, merge, publish, distribute, sublicense,
# or exploit this code without Hanhan Wu's EXPLICIT written permission.

import openai
from concurrent.futures import ThreadPoolExecutor, as_completed

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams, LLMTestCase

model_str = 'gpt-4.1-nano'


def my_deepeval_answer_correctness(question, context, ground_truth, answer):
    correctness_metric = GEval(
		    name="Answer Correctness",
            model=model_str,
		    criteria="""Determine whether the key points of the answer aligns with the key points of the ground_truth and the context. 
                        If the question is asking for a number, as long as the answer's number matches the ground_truth's number, it is considered correct.
                """,
		    evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT,
						       LLMTestCaseParams.EXPECTED_OUTPUT,
                               LLMTestCaseParams.CONTEXT],
		)
    test_case = LLMTestCase(
        input=question,
        context=context,
        actual_output=answer,
        expected_output=ground_truth)
    correctness_metric.measure(test_case)
    score = correctness_metric.score
    eval_reason = correctness_metric.reason

    return score, eval_reason


def get_gpt_answer(prompt_template, question, context, model="gpt-4.1-nano"):
    full_prompt = f"""{prompt_template}

        Context:
        {context}

        Question:
        {question}
        """
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=128,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
