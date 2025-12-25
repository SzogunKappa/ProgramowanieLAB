import datetime
ostatnie_lab = datetime.datetime(2026,1,17)
do_kolo = ostatnie_lab-datetime.datetime.now()

class data:
    def __init__(self,czas:datetime.datetime):
        self.czas = czas
        print(self.czas.days)
    def __str__(self):
        return f"dni: {self.czas.days}"

test = data(do_kolo)
print(test)