import requests
url = "http://localhost:3000/cars/6"
try:
	reply =requests.get(url)
except:
	print("Halozati hiba")
	exit()
print (reply.status_code)
print (reply.text)
