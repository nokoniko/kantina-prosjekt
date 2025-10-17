class Liste:
    def __init__(self, name) -> None:
        self.name = name


    menyen = [
        {"navn": "Andeconfit", "kategori": "Varmrett", "allergener": ["gluten", "melk"], "bilde": "andeconfit.jpeg", "dag": "Mandag"},
        {"navn": "Coq au vin", "kategori": "Varmrett", "allergener": [], "bilde": "coq_au_vin.jpg", "dag": "Tirsdag"},
        {"navn": "Hokkaido-suppe", "kategori": "Suppe", "allergener": ["melk"], "bilde": "hokkaido_suppe.jpeg", "dag": "Onsdag"},
        {"navn": "Bœuf bourguignon", "kategori": "Varmrett", "allergener": [], "bilde": "boeuf_bourguignon.jpg", "dag": "Torsdag"},
        {"navn": "Ratatouille", "kategori": "Vegetarrett", "allergener": [], "bilde": "ratatouille.jpg", "dag": "Fredag"}
    ]

    varere = [
        {"navn": "Sjokolademelk", "kategori": "Drikke", "allergener": ["melk"], "pris": 25},
        {"navn": "Eplejuice", "kategori": "Drikke", "allergener": [], "pris": 20},
        {"navn": "Mineralvann", "kategori": "Drikke", "allergener": [], "pris": 22},
        {"navn": "Nøtteblanding", "kategori": "Snack", "allergener": ["nøtter"], "pris": 30},
        {"navn": "Yoghurt med granola", "kategori": "Snack", "allergener": ["melk", "gluten", "nøtter"], "pris": 35},
        {"navn": "Croissant", "kategori": "Bakverk", "allergener": ["gluten", "melk"], "pris": 28},
        {"navn": "Baguette med ost og skinke", "kategori": "Mat", "allergener": ["gluten", "melk"], "pris": 55},
        {"navn": "Salatboks", "kategori": "Mat", "allergener": ["egg"], "pris": 60},
        {"navn": "Fruktbeger", "kategori": "Snack", "allergener": [], "pris": 30},
        {"navn": "Kaffe", "kategori": "Drikke", "allergener": [], "pris": 20},
        {"navn": "Te", "kategori": "Drikke", "allergener": [], "pris": 18},
        {"navn": "Brownie", "kategori": "Bakverk", "allergener": ["gluten", "melk", "egg"], "pris": 32}
    ]

