from flask import render_template
import datetime

class Hjelp:
    def __init__(self, name) -> None:
        self.name = name

    # lager en variablen som hetter dag. den får hvulken dag det er med å bruke datetime.
    dag = datetime.datetime.now().strftime("%A")
    def dagmeny(self) -> str:
        """
        lager en funskjon som bruker den lokale variablen dag den matcher hvilken dag det er og retunerer den rikitge nettsiden får den dagen
        """
        match self.dag:
            case "Monday":
                return render_template('retter/andeconfit.html')
            case "Tusday":
                return render_template('retter/coq_au_vin.html')
            case "Wednesday":
                return render_template('retter/hokkaido_suppe.html')
            case "Thursday":
                return render_template('retter/boeuf_bourguignon.html')
            case "Friday":
                return render_template('retter/ratatouille.html')


if __name__ == "__main__":
    h = Hjelp(__name__)
    print(h.dag)