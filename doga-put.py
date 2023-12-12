import requests, json

adatb ={
            "id": 1,
            "name": "Mariadb",
            "type": "RDBMS"
        }
adat=json.dumps(adatb)

h={"Content-Type":"application/json"}
try:
	reply=requests.put("http://localhost:3000/databases/1",headers=h, data=adat)
except:
	print("Hiba tortent")
	exit()

print(reply.status_code)
