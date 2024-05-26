### Deploy the App

Time to deploy the app so that it's accessible to the public!

1. Make sure your code is saved as a public Github repo [like this][1].
2. [Create your Streamlit account][2].
3. After logging in, click <b>Create app</b> and a form will pop up where you can fill out the Github repo link, homepage file name and customize your app's URL. Click <b>Advanced settings...</b> and then <b>Secrets</b> to save the credentials. To call these credentials in the code, you just need `import streamlit as st` and then use `st.secrets['<credential name>']`. After clicking <b>Deploy!</b>, you app will become public soon! 🎉
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/app_deploy1.png" width="1048" height="688" />

4. After the app went public, if you want to allow the public to fork your Github repo. Go to your Streamlit account and you will see an orange triangle near <b>Workspaces</b>, click <b>Settings</b> in the dropdown menu, and then login to your Github account where saves this app's code. After this authorization, you should be able to see the Github logo at the top right corner of your app.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/app_deploy2.png" width="1058" height="230" />

5. Sometimes, you want to update the settings of your app, such as secrets

[1]:https://github.com/lady-h-world/My_Garden_LocalStream_App
[2]:https://share.streamlit.io/signup