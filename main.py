from time import sleep
from app.request import *
from app.cv import *
from app.client.upload import *
from app.scrapping import *

scrape_assets() # Geração de Uid
while True:
    scrapping() # Download Template
    sobrepor() # Dmca
    name = response()
    create(name)
    sleep(60)
    
