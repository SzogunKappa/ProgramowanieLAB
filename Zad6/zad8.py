import keyword
listword = ["for","print","break","done","bad"]
for x in listword:
    print(f"{x} is a keyword = {keyword.iskeyword(x)}")
