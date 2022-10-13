"""oef 1
getal = int(input("geef een getal in"))
if getal%3==0:
    print("deelbaar door 3")
else:
    print("niet deelbaar door 3")"""

"""
oefening 2
km = float(input("geef het aantal km in"))
prijs = 0
if km < 26:
    prijs = km*0.25
else:
    km = km - 25
    prijs = 6.25+km*0.15
print("prijs : € {}".format(round(prijs,2)))
"""
a = 9
b = 12
c = 14

if a > b:
    if a > c:
        print("getal a is het grootste")
elif b > a:
    if b > c:
        print("getal b is het grootste")
elif c > a:
    if c > b:
        print("getal c is het grootste")


