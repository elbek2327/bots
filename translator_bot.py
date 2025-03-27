import os
# from dotenv import load_dotenv
# import  json
import  requests
app_id = os.getenv("TRANSLATOR_APP_ID")
app_key =  	os.getenv("TRANSLATOR_API_KEY")
endpoint = "entries"
language_code = "en-gb"
word_id = "None"
url = "	https://od-api-sandbox.oxforddictionaries.com/api/v2" + endpoint + "/" + language_code + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print("code {} \n ".format(r.status_code))