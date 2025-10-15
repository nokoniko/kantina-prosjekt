import datetime

class Hjelp:
    def __init__(self, name) -> None:
        self.name = name


    dag = datetime.datetime.now().strftime("%A")




h = Hjelp(__name__)
print(h.dag)