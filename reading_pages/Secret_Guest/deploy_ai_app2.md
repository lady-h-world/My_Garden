### How to Build Local Stream
#### Set Up
1. To develop and deploy the app for free, we can use <b>Streamlit</b>, a platform that enables data scientists to create apps in Python. Installation is straightforward, requiring only `pip install streamlit`.
2. In order to be able to recommend local traveling activities, ChatGPT provides most intelligent results, particularly when seeking recommendations tailored to the selected season. [Go through these steps][1] to create an OpenAI account and ensure there are funds in your billing account, but don't worry, ChatGPT is cost-effective, it only charges $0.01 USD every 4, 5 queries from Local Stream.
3. In order to find photos related to ChatGPT's recommendations, [Apify's Google Image Scraper][2] provides the most relevant results. Simply [create a free account on Apify][3], then navigate to <b>Settings</b> and click <b>Integrations</b> to obtain your <b>API Token</b>. Apify is a web scraping platform that offers frameworks for users to utilize or develop web scrapers to extract data from the Internet. Apify provides $5 dollars monthly for you to use, so if your app is not too popular, this free $5 should be enough, otherwise [you can check Apify pricing choices][8] for your purpose.
4. (Optional) If you want to save money, after Apify used up monthly $5, you can keep using Google Custom Search, it allows daily 100 free requests! In order to use it, you need to [create a Google Search API key][9] and [create a search engine to get its ID][10].
5. Key packages to install:
* `pip install pydeck` to enable the display of suggested locations on the map.
* `pip install openai` to use OpenAI API.
* `pip install streamlit-extras` to use extra features of Streamlit.
* `pip install apify-client` to access Apify API.
* `pip install pillow` to enable image display from image URLs.


#### Code Structure
To make Streamlit app work, you need to follow a few rules in the code structure:
* List all the required python packages in [requirements.txt][4] file, along with the version of each package specified. This file will be used to establish the environment during the app deployment stage.
  * After installing all the required packages, Lady H. normally run command `pip freeze >> requirements.txt` to generate this file.
* Create a .py file as the app's home page, such as the "explore.py" shown below.
* Create a folder named <b>"pages"</b> to store all app pages except the home page, each page is a .py file too. 
  * The folder name here has to be "pages", otherwise Streamlit can't locate the pages 😉. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/streamlit_code_structure.png" width="359" height="203" />

🌻 [Check Local Stream's code structure here >>][5]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][6]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][7]

[1]:https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt
[2]:https://apify.com/hooli/google-images-scraper
[3]:https://console.apify.com/sign-up
[4]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/requirements.txt
[5]:https://github.com/lady-h-world/My_Garden_LocalStream_App
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app3.md
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app1.md
[8]:https://apify.com/pricing?utm_term=apify%20pricing&utm_campaign=TOP-EN+%7C+SEA+%7C+Brand+%7C+Others&utm_source=google&utm_medium=ppc&hsa_acc=9303439903&hsa_cam=21163808628&hsa_grp=161370239672&hsa_ad=696046221522&hsa_src=g&hsa_tgt=kwd-1063512148937&hsa_kw=apify%20pricing&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjw0YGyBhByEiwAQmBEWh58kvXCW-qS61SUQBuTXm5C8fANjsfLp0xNl3F-kPyn-wc3np-SlxoC__4QAvD_BwE
[9]:https://console.cloud.google.com/apis/credentials?project=defcon-videolist
[10]:https://programmablesearchengine.google.com/controlpanel/all