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
* In `get_geo_json()`:
  * The geo information can be generated from this type of url `https://nominatim.openstreetmap.org/?addressdetails=1&q={dest}+{region}+{country}&format=json&limit=1`, it's a service provided by Nominatim.
  * In order to use 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ls_results_code2.png" width="1100" height="900" />

🌻 [Check utils code here >>][2]


[1]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/pages/results.py
[2]:https://github.com/lady-h-world/My_Garden_LocalStream_App/blob/main/utils.py
[3]:https://platform.openai.com/docs/models
