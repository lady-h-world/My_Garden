### 💝 A Product Design Story
<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/product_design.png" width="276" height="261" /></p>

Local Stream is a simple app, but before achieving this result, Lady H. failed the 3 versions because they can't achieve smooth user experience. The key of building a product no longer stays at achieving model performance, we have to keep a good balance between smooth user experience and satisfying model performance. Because missing either factor, users won't use your app.

Initially, Lady H. plans to use Instagram to show local activities, because it provides fun photos taken by ordinary people in a wide variety of traveling spots, the photos are up-to-date and it's free. In order to search for most relevant photos from Instagram, Lady H. tried sentiment analysis and different ranking formulas. However, Instagram provides strong security settings that once it detects activities like bots, it requires different kinds of manually authentication, and Lady H. couldn't find a way to automatically bypass the authentication requests. 


Here are the examples of image search using Instagram:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ins_image_search.png" width="731" height="814" />

It is indeed a pity for not able to use Instagram photos in this app. However, often times, bad news will become good news! Lady H. later found the image search results provided by Apify Image Scraper or Google Custom Search are both more relevant and more specific than Instagram. Besides, to achieve current user experience, Lady H. went through trails and errors to test how to ensure image search quality while shorten image search & loading time.

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/loggin_off.png" width="252" height="237" /></p>

Even OpenAI wasn't the initial choice to suggest local travel locations and activities. Lady H. tried web scraping to extract recommendations from popular travel websites, also tried famous tools such as [Langchain][1]. But finally considering output quality, user experience and financial cost, Lady H. considers OpenAI API as the best choice.

Every simple product has a story of efforts spent behind. During the app design and development stage, Lady H. can't stop thinking about new ideas to make further improvement. Even now, she has a list of to-dos for the future.

Also keep in mind friends, sometimes, you need to take a good rest first, and after returning back to work, you will have even better ideas!


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Secret Guest Home >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]

[1]:https://github.com/langchain-ai/langchain
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/secret_guest.md#sprouts-collection-time
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app6.md