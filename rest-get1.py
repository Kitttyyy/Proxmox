#!/usr/bin/env python3
import requests

url="https://cat-facts.herukoapp.com/facts"
hr1= {"Connection":"keep-alive"}
hr2={"Connection":"close"}
try:
	reply=requests.get(url, headers=hr2)
except:
	print("Hiba!")
	exit()
print(reply.status_code)

if reply.status_code == 200:
	print(reply.json())
