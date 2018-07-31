number = { "n1":1, "n2":2}
print(number["n1"])

number["n3"] = 3
print(number)

#number["n3"] = 4
#print(number)

del number["n1"]
print(number)
number["n1"] = 1

for a in number.keys():
    print(a.lower())

if "n3" in number.keys():
    print("ok")
else:
    print("no")

for a in number.values():
    print(a)