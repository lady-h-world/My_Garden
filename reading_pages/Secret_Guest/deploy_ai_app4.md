### Build Results Page

The code below has the key logic of recommendation generation and map display.
* `get_llm_suggests()` uses OpenAI to suggest traveling locations in your destination and local activities in each location.
* `get_geo_json()` uses Nominatim, a geocoding software to find the latitude and longitude of each suggested location.
* `get_map()` will create a map based on locations' latitude and longitude, then Streamlit built-in `pydeck_chart()` will display the map.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_results_code1.png" width="1000" height="500" />

🌻 [Check results page code here >>][1]

The code below shows the implementation of the 3 functions highlighted above, they are implemented in `utils.py`.
* In `get_llm_suggests()`:
  * Model was using GPT-3.5 Turbo, you can choose more advanced models [here][3].
  * `messages` creates the query that searches for best activities to do in user specified region & country & month, as well as listing all those activity locations.
  * It returns suggested location list and detailed suggestions separately.
* If suggested location list is not empty, `get_geo_json()` generates geo information using Nominatim service:
  * In order to use Nominatim, you have to specify User-Agent header to identify yourself, this helps the service track usage and enforce usage policies. Since its main purpose is to identify the user, your can use your email address as the value of `User-Agent`.
    * In the code below, Lady H.'s header was saved in Streamlit secrets `st.secrets['PYDECK_UA']` in order to keep it private. You will see details in later deployment section.
  * The geo information can be generated from this type of url `https://nominatim.openstreetmap.org/?addressdetails=1&q={dest}+{region}+{country}&format=json&limit=1`, it only needs to fill in the `dest`, `region` and `country`.
  * Its output is a pandas dataframe that stores each suggested location (`dest`), together with its latitude and longitude.
* `get_map()` loads the output of `get_geo_json()`, with known latitude and longitude of each location, it creates a map using `pydeck`.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_results_code2_v2.png" width="1061" height="777" />

🌻 [Check utils code here >>][2]

After loading the map, if the suggestion is not empty, then it's time to show photos of the suggested local activities. For this app, Lady H. prefers to do up-to-date photo search, so that users can feel better about what's happening in the local recently. That's also why the app is called as "Local Stream". Considering price, image search quality and speed, Lady H. found 2 available solutions:
* Apify enabled image search
* Google Custom Search enabled image search

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_results_code2_v2.png" width="1044" height="777" />

[1]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/pages/results.py
[2]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/utils.py
[3]:https://platform.openai.com/docs/models
