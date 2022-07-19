import requests

gorgon = requests.post(
    url = 'https://xtekky.com/xgorgon/v2',
    data = {
        "params": "userid=xxxx&version=9293&etc...",
        "data": None, # POST data (urlencoded)
        "cookies": "sessid=xxxxx; odin-tt=xxxxx;"
    }
).json()
print(gorgon)
