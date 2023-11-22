#!/usr/bin/env python3
# elso programunk
a=input("Adj meg egy fajl nevet: ")
try:
	with open(a) as f:
		a= f.readline()
except IOError:
	print("I/O hiba!")
	exit()
except:
	print("Valamilyen hiba")
	exit()
def teszt(a, b, c=3):
	print(a, b, c)
teszt(1, 2, c = "pisti")
print(a, sep = " ", end = "\n")

