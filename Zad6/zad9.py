import random
start = int(input("Podaj min"))
stop = int(input("Podaj max"))+1
tup = tuple(x for x in range(start,stop))
tup_all = 1
for x in tup:
    tup_all=tup_all*x
print("średnia: ",tup_sum)
