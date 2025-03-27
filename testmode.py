import jovian
import requests
# from pprint import pprint as print
# import os


jovian.commit(project="telegram-03-apis")
city='tashkent'

url = f"https://api.pray.zone/v2/times/today.json?city={city}&school=5"
r = requests.get(url)
print(r.status_code)
