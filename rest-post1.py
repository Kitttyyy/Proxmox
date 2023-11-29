import requests
d = {"id":1,"brand":"Lada", "model":"Riva", "production_year":1980, "convertible":False}
h = {"Content-type":"application/json"}
url = "http://localhost:3000/cars"
reply = requests.post(url, json=d, headers=h)
print(reply.status_code)
