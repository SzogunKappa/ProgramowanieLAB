import time
def sekundnik(sec):
    for x in range(sec):
        print(sec-x)
        time.sleep(1)
    print("BOOOM")

sekundnik(10)