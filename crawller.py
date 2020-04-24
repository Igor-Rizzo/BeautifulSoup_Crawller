#importar as Libs
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = urlopen('https://g1.globo.com/') #definindo um site como alvo
bs = BeautifulSoup(html.read(), "html.parser")

body = bs.body

for noticiaTitulo in body.find_all("a", class_='feed-post-link gui-color-primary gui-color-hover') :
    print(noticiaTitulo.text)