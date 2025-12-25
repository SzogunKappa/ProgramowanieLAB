import random
start = int(input("Podaj min"))
stop = int(input("Podaj max"))+1
tup = tuple(random.randint(start,stop) for x in range(10))
tup_all = 1
for x in tup:
    tup_all=tup_all*x
print("średnia: ",tup_all**(1/len(tup)))
