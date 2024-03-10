from bs4 import  BeautifulSoup
import requests

response = requests.get('https://www.roblox.com/catalog/').text

soup = BeautifulSoup(response, 'html.parser')

# Encontrar a tag 'meta' com o atributo 'name' igual a 'twitter:title'
meta_tag = soup.find('meta', {'name': 'twitter:title'})

# Verificar se a tag foi encontrada e extrair o conteúdo da tag 'content'
if meta_tag:
    content_text = meta_tag['content']
    print(content_text)