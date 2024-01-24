#!/usr/bin/env python3
import requests

url = "https://postman-echo.com/basic-auth"
user = "postman"
password= "password"

r = requests.get(url, auth=(user, password)) 

print(r.status_code)
print(r.json())
