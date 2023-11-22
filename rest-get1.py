#!/usr/bin/env python3
import requests

url="https://cat-facts.herukoapp.com/facts"

try:
	reply=requests.get(url)
except:
	print("Hiba!")
	exit()
print(reply.status_code)
try:
	print(reply.json())
except:
	print("Nincs ervenyes JSON adatunk")
	exit()
