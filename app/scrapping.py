import requests, random
import json 
import json
import random
import requests

def scrape_assets():
    
    with open('config/handler.json') as arquivo_json:
        dados = json.load(arquivo_json)
        result = dados['image']['Search']['Active']
        keywords = dados['image']['Search']['keywords']
        subcategory = dados['image']['Search']['subcategory']

    if result == True:
        cookie = jsondump()
        items = requests.get(f"https://catalog.roblox.com/v1/search/items?category=Clothing&limit=120&salesTypeFilter=1&sortAggregation={random.choice(['1', '3', '5'])}&sortType={random.randint(0, 2)}&subcategory={subcategory}&minPrice=5&keyword={keywords}", 
                            cookies={".ROBLOSECURITY": cookie}, 
                            headers={"x-csrf-token": generate_token()})
        if items.status_code == 200:
            ids = [item['id'] for item in items.json()["data"]]
            with open('config/uid.json', 'w') as uid_file:
                json.dump(ids, uid_file, indent=4)
            return ids
        else:
            return []
    elif result == False:
        with open('config/handler.json') as arquivo_json:
            dados2 = json.load(arquivo_json)
            result2 = dados2['image']['Search']['Database']['Uid']
            with open('config/uid.json', 'w') as uid_file2:
                json.dump(result2, uid_file2, indent=4)
            return result2

def jsondump():
    with open('config/handler.json') as arquivo_json:
        dados = json.load(arquivo_json)

    cookies = dados['user']['Cookie']
    return cookies 

def generate_token():
    cookie = jsondump() 
    response = requests.post("https://economy.roblox.com/", cookies={".ROBLOSECURITY": cookie})
    _x_token = response.headers.get("x-csrf-token")
    return _x_token

cookie = jsondump()


