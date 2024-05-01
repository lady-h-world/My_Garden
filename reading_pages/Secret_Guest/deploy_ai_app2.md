### How to Build Local Stream
#### Set Up
1. To develop and deploy the app for free, we can utilize <b>Streamlit</b>, a platform that enables data scientists to create apps in Python. Installation is straightforward, requiring only `pip install streamlit`.
2. To recommend local activities in a travel destination, using ChatGPT can get more insightful results, particularly when seeking recommendations tailored to the selected season. [Go through these steps][1] to create an OpenAI account and ensure there are funds in your billing account, and don't worry, ChatGPT is cost-effective, it only charges $0.01 USD every 4, 5 queries from Local Stream.
3. In order to find photos related to ChatGPT's recommendations, [Apify's Google Image Scraper][2] provides the most relevant results. Simply [create a free account on Apify][3], then navigate to <b>Settings</b> and click <b>Integrations</b> to obtain your <b>API Token</b>. Apify is a web scraping platform that offers frameworks for users to utilize or develop web scrapers to extract data from the Internet.
4. Other packages need to install:
* `pip install pydeck` to enable the display of suggested locations on the map
* `pip install openai` in order to use OpenAI API
* `pip install streamlit-extras` to use extra features of Streamlit
* `pip install apify-client` to access Apify API
* `pip install pillow` to enable image display from image URL


#### Code Structure
To make Streamlit app work, you need to follow a few rules of the code structure:
* List all the required python packages in [requirements.txt][4] file, along with the version of each package specified. This file will be used to establish the environment during the app deployment stage.
  * To save efforts, after installing key packages listed in above 4th step, Lady H. normally run command `pip freeze >> requirements.txt` to generate this file.
* Create a .py file as the app's home page, such as the "explore.py" shown below.
* Create a folder named <b>"pages"</b> to store all app pages except the home page, each page is a .py file too. 
  * The folder name here has to be "pages", otherwise Streamlit can't locate the pages. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/streamlit_code_structure.png" width="359" height="203" />

[1]:https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt
[2]:https://apify.com/hooli/google-images-scraper
[3]:https://console.apify.com/sign-up
[4]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/requirements.txt
