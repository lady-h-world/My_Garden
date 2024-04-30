### How to Build Local Stream
#### Set Up
1. To develop and deploy the app for free, we can utilize <b>Streamlit</b>, a platform that enables data scientists to create apps in Python. Installation is straightforward, requiring only `pip install streamlit`.
2. To recommend local activities in a travel destination, using ChatGPT can get more insightful results, particularly when seeking recommendations tailored to the selected season. [Go through these steps][1] to create an OpenAI account and ensure there are funds in your billing account. Fortunately, ChatGPT is cost-effective, charging only $0.01 USD every 4 to 5 queries from Local Stream.
3. In order to find photos related to ChatGPT's recommendations, [Apify's Google Image Scraper][2] provides the most relevant results. Simply [create a free account on Apify][3], then navigate to <b>Settings</b> and click <b>Integrations</b> to obtain your <b>API Token</b>. Apify is a web scraping platform that offers frameworks for users to utilize or develop web scrapers to extract data from the Internet.
4. Other packages need to install:
* `pip install pydeck` to enable the display of suggested locations on the map
* `pip install openai` in order to use OpenAI API
* `pip install streamlit-extras` to use extra features of Streamlit
* `pip install apify-client` to access Apify API
* `pip install pillow` to enable image display from image URL

[1]:https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt
[2]:https://apify.com/hooli/google-images-scraper
[3]:https://console.apify.com/sign-up
