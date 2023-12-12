#!/usr/bin/env python3
import requests

bekert=input("Melyik sorszamu adatot akarod torolni?")
url="http://localhost:3000/databases/"
h={"Connection":"keep-alive"}

try:
        reply=requests.delete(url + bekert, headers=h)
except:
        print("Hiba tortent")
        exit()

print(reply.status_code)
