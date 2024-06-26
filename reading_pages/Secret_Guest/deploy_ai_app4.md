### Build Home Page

Every page in Streamlit has 2 components:
* 1st component: The side bar on the left. 
  * Streamlit will automatically detect all of your web pages and list them on the side bar.
  * You can decide which elements to show on the side var, such as the logo, required user input, etc.
* 2nd component: The main web elements are on the right side.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/local_stream_interface1.png" width="997" height="296" />

The user interface for Local Stream is straightforward. Users need to input their destination country and the month of their intended travel. Additionally, they can further specify the particular region within the country they wish to visit.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_homepage_input_v2.png" width="1037" height="412" />

Now let's break down the code of this home page to learn how to build an app through Streamlit.

🌻 [Check home page code here >>][1]

In the code below:
* Line 4 specifies the page title, which will be displayed in the user's browser tab.
* Line 5 ~ 7 shows how can we add elements in sidebar. The code here is adding the logo image there.
* Line 13 ~ 15 is trying to set the default value of "show_region", you will see this web element later. This settings means, by default, the user won't specify the traveling region. It is important to highlight the use of `st.session_state`, it stores all variables that can be shared within a user session, allowing these variables to be accessed across different pages of the app and ensuring their values remain consistent throughout a user session.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_home_code1.png" width="993" height="436" />

Line 19 ~ 72 creates the web elements on home page:
* Line 19 creates a table of 2 columns.
* In the first column `col1`:
  * A `text_input` is created to submit "Country" value, once the value is submitted, this text input will be cleared. Streamlit provides multiple ways for users to submit the value: they can press 'Enter', 'Tab', or simply move the mouse out of the input field.
  * After the user filled in the country value, a `radio` button will appear, asking whether to specify specific region. By default, its value is "No", as specified in line 15.
  * If the user choose "Yes" in the radio button, another `text_input` will appear to let the user fill in the region.
  
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_home_code2.png" width="946" height="686" />

And in the second column `col2`, a `selectbox` is created to allow the user to choose the traveling month.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_home_code3.png" width="938" height="310" />

The last component of the home page enables input confirmation and input clean up:
* Line 76 ~ 88 will display the user's input, including country, region and selected month.
* Line 91 ~ 100 cleans up user input. By clicking "Clear Input" button, the user interface will clean up all the user input.
* After the user has entered all the required information, a "CONFIRM" button will appear. Upon clicking this button, the user interface will switch to the results page.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_homepage_code4_v2.png" width="1022" height="657" />

🌻 [Check home page code here >>][1]


The loaded results page will showcase a map featuring all the suggested spots at the travel destination. This map offers an overview. Subsequently, for each suggestion, 1 or 2 photos depicting local activities will visualize the suggested experience to users!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_results.png" width="919" height="642" />

Now let's see how to implement the output page!


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]

[1]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/explore.py
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app5.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/deploy_ai_app3.md
