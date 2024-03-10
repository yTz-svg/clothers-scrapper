import requests
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json 


def getname(uid):
    response = requests.get(f'https://www.roblox.com/catalog/{uid}').text
    soup = BeautifulSoup(response, 'html.parser')

    meta_tag = soup.find('meta', {'name': 'twitter:title'})

    if meta_tag:
        content_text = meta_tag['content']
        with open('img/cache/name.txt', 'w') as file:
            file.write(content_text)

def response():
    with open('img/cache/name.txt', 'r') as file:
        content = file.read()
        return content


def scrapping():
    with open('config/uid.json') as uid_file:
        ids = json.load(uid_file)

    assetIDs = []

    if ids:
        assetID = ids.pop(0)  
        url = f'https://assetdelivery.roblox.com/v1/assetId/{assetID}'
        getname(assetID)
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.text
            ExtrairXml(data[13:67])
            assetIDs.append(assetID)

    with open('config/uid.json', 'w') as uid_file:
        json.dump(ids, uid_file)

    return assetIDs


def ExtrairXml(url):
    response = requests.get(url)
    xml_data = response.text
    root = ET.fromstring(xml_data)
    url_element = root.find('.//Content/url') 
    if url_element is not None:
        imgURL = re.search(r'\?id=(\d+)', url_element.text).group(1)
        RetornaUrl(imgURL)

def RetornaUrl(ID):
    url = 'https://www.roblox.com/library/' + ID
    response = requests.get(url)
    print(response)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')    
    img_element = soup.find('img')

    if img_element:
        template = img_element['src']
        response = requests.get(template)
        with open('img/cache/shirt.png', 'wb') as file:
            file.write(response.content)

