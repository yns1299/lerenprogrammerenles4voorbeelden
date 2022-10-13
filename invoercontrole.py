"""invoer = ""
som = 0
while not invoer == "stop":
    invoer = input()
    if invoer == "stop":
        break
    else:
        try:
            invoer = int(invoer)
            som += invoer
        except ValueError:
            print("gelieve een geheel getal in te geven")
print(som)
"""
import random as rnd
a = rnd.randint(10000,1000)
b = rnd.randint(10000,1000)
c = rnd.randint(10000,1000)
if a > b and a > c:
    print(a,b,c,"a grootste")
if b > a and b > c:
    print(a,b,c,"b grootste")
if c > a and c > b:
    print(a,b,c,"c grootste")
