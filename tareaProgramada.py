from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import requests
import names
import tkinter
url = "https://www.tec.ac.cr/planes-estudio"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
cuadros = soup.find_all ("div", class_ = "group")
info = ""
for i in cuadros:
    info += i.text
info = info.split("\n")
lista = []
for i in info:
    if i != "":
        lista.append(i)

print(lista)
def prueba():
    print('prueba mod 12')