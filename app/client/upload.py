import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from time import sleep

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

def create(name):
    cookie = jsondump()
    payload = {
        "assetType": 'shirt',
        "creationContext": {
            "creator": {
                "groupId": 9511637
            },
            "expectedPrice": 10
        },  
        "description": 'tags: free, pants, kawaii, cute, shirt, dior, fashion, angel, kawaiicore, heart, vibe, dollcore, dolly, shirt, cutesy, love, cottage, cottagecore, pastel, luxury, adorable, runway, couture, leather, aesthetic, cool, queen, jean, eagle, admin, vip, funny, camo, army, pirate tix, awesome, jacket, Skinny, Emo, Zombie, paris hilton, y2k, slender, barbie, model, avengers, x-men, superhero, villain, marvel, aesthetic, galaxy, pink ,blue crop top, pretty, emo, goth, scary, blood, christmas, santa, winter, snow, suit, white, mr calus, claus, corgi, dog, animal, cat, elephant, zoo, animals, lion, tiger, monkey, giraffe, gorilla, turtle, duck, penguin, cow, sweater, assassin, halloween, haloween, haallowen, orange, fall, cold, overalls, war, rainbow, korean, soviet, ww2, ww1,',
        "displayName": name
    }
    
    headers = {'X-CSRF-TOKEN': generate_token()}
    multipart_data = MultipartEncoder(
        fields={
            'request': json.dumps(payload),
            'fileContent': ('shirt.png', open(f'img/result/name.png', 'rb'),'image/png')
        }
    )
    
    headers['Content-Type'] = multipart_data.content_type
    
    dd = requests.post("https://apis.roblox.com/assets/user-auth/v1/assets", data=multipart_data, headers=headers, cookies={".ROBLOSECURITY": cookie})
    dd_json = dd.json()
    print(dd_json)
    operation_id = dd_json.get('operationId')
    sleep(30)
    data22 = requests.get(f"https://apis.roblox.com/assets/user-auth/v1/operations/{operation_id}", headers={'X-CSRF-TOKEN': generate_token()}, cookies={".ROBLOSECURITY": cookie})
    data33 = data22.json()
    asset_id = data33['response']['assetId']
    print(f'[+] Publicado com sucesso {operation_id}, id: {asset_id}')
    publish(asset_id)


def publish(asset_id):
    cookie = jsondump() 
    xcrf = generate_token() 
    headers = {
        "X-CSRF-TOKEN": xcrf,
        "Content-Type": "application/json",
        "Cookie": f".ROBLOSECURITY={cookie};"
    }
    data = {
        "saleAvailabilityLocation": [0, 1],
        "priceConfiguration":
            {"priceInRobux": 5},
        "saleStatus": "OnSale"
    }
    return requests.post(f"https://itemconfiguration.roblox.com/v1/assets/{asset_id}/release", headers=headers, json=data)
    


"""
        headers = headers
        headers["x-csrf-token"] = headers
        headers["Accept"] = "*/*"
        headers["Pragma"] = "no-cache"
        headers["Origin"] = "create.roblox.com"
        headers["Referer"] = "https://create.roblox.com/"

        request_data = json.dumps({
            "displayName": 'olola',
            "description": 'lerolerolero',
            "assetType": 'shirt',
            "creationContext": {
                "creator": {"groupId": 9511637},
                "expectedPrice": 10
            }
        })

        upload_req = requests.post(
            url="https://apis.roblox.com/assets/user-auth/v1/assets",
            headers=headers,
            files={"fileContent": ("img/cache/shirt.png"), "request": (None, request_data)},
        )
        print(upload_req)
"""