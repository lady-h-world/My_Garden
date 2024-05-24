### How to Build Local Stream
#### Set Up
##### 1. Install Streamlit
To develop and deploy the app for free, we can use <b>Streamlit</b>, a platform that enables data scientists to build and publish apps in Python. Installation is straightforward, requiring only `pip install streamlit`.

##### 2. Create and Fund OpenAI Account
In order to intelligently recommend local traveling activities, ChatGPT is a good choice, particularly when seeking recommendations tailored to the selected season. [Follow this tutorial][1] to:
* create an OpenAI account
* create and save the API key
* setup billing and fund your OpenAI account

Does word like "billing", "funding" sound scary 💸🤑? Don't worry! ChatGPT is cost-efficient. For the usage in Local Stream, it only charges $0.01 USD every 4, 5 queries.

##### 3. Enable Apify Image Scraper 
Apify's image scraper delivers high quality image search results. This appears not only in the images' resolution but also their relevance to the search queries. To set up this scraper:
* Click <b>Try for free</b> in [Apify's Google Image Scraper][2] and sign up for the free account.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify1.png" width="495" height="170" />

* After login, you should be able to see <b>Google Images Scraper</b> in your <b>Actors</b>.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify2.png" width="626" height="344" />

* Click <b>Google Images Scraper</b>, then click <b>Runs</b>, followed by clicking <b>Start Actor</b>.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify3.png" width="959" height="403" />

* Next, you will see a page where you mainly need to click <b>Save & Start</b> to start the actor. Before clicking this button, you can also specify the image search query and maximum number of returned results. In this example, Lady H. was searching for 2 images of "Canada".
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify4.png" width="429" height="395" />

* After the actor had been built successfully, you will be directed to the <b>Output</b> page, like this:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify5.png" width="1031" height="209" />

* Now go to <b>Settings</b> to get your API token.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify6.png" width="927" height="315" />

* Apify even prepared the while piece of code for you to copy in order to use this scraper. Go back to <b>Google Images Scraper</b> and click <b>API</b> in the top right corner. Then click <b>API clients</b> from the dropdown menu.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify7.png" width="967" height="253" />

* The code template written in different languages will appear, choose <b>Python</b> and copy the code there. To execute this scraper, you only need to replace "<YOUR_API_TOKEN>" with your own API token.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/apify8.png" width="711" height="536" />

Apify provides $5 dollars monthly for you to use, so if your app is not too popular, this free $5 should be enough as each image search only costs $0.003. Otherwise [you can check Apify pricing choices][8] for your purpose. 😉 Tip, you can also create multiple accounts to use the free service for a longer term 😉.

##### 4. (Optional) Enable Google Custom Search
There is very low chance that Apify doesn't return output, such as having timeout error. Low chance doesn't mean 0 possibility, and when it happened it hurts user experience. To ensure a smooth user experience, we can use an alternative image search solution. Among all the free solutions, Lady H. chose Google Custom Search, because it's fast and allows 100 free queries each day. In order to use it, you need to [create a Google Search API key][9] and [create a search engine to get its ID][10].


##### 5. Other Key Packages to Install
Besides package "streamit", you also need to install the following packages:
* `pip install pydeck` to enable the display of suggested locations on the map.
* `pip install openai` to use OpenAI API.
* `pip install streamlit-extras` to use extra features of Streamlit.
* `pip install apify-client` to access Apify API.
* `pip install pillow` to enable image display from image URLs.


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
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app3.md
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app1.md
[8]:https://apify.com/pricing?utm_term=apify%20pricing&utm_campaign=TOP-EN+%7C+SEA+%7C+Brand+%7C+Others&utm_source=google&utm_medium=ppc&hsa_acc=9303439903&hsa_cam=21163808628&hsa_grp=161370239672&hsa_ad=696046221522&hsa_src=g&hsa_tgt=kwd-1063512148937&hsa_kw=apify%20pricing&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjw0YGyBhByEiwAQmBEWh58kvXCW-qS61SUQBuTXm5C8fANjsfLp0xNl3F-kPyn-wc3np-SlxoC__4QAvD_BwE
[9]:https://console.cloud.google.com/apis/credentials
[10]:https://programmablesearchengine.google.com/controlpanel/all
