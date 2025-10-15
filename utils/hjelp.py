from flask import render_template
import datetime

class Hjelp:
    def __init__(self, name) -> None:
        self.name = name

    dag = datetime.datetime.now().strftime("%A")

    def dagmeny(self) -> str:
        match self.dag:
            case "Monday":
                return render_template('mandag.html')
            case "Tusday":
                return render_template('tirsdag.html')
            case "Wednesday":
                return render_template('onsdag.html')
            case "Thursday":
                return render_template('torsdag.html')
            case "Friday":
                return render_template('fredag.html')


if __name__ == "__main__":
    h = Hjelp(__name__)
    print(h.dag)