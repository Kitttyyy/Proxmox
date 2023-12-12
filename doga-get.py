#!/user/bin/env python3
import requests

url="http://localhost:3000/adatb/"
h={"Connection":"keep-alive"}

try:
	reply=requests.get(url, headers=h)
except:
	print("Hiba tortent")
	exit()

print(reply.status_code)
