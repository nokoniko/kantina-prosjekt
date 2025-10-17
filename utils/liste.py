class Liste:
    def __init__(self, name) -> None:
        self.name = name

    # lagger 2 lister den enne til mat menyen og den adnre til de faste varerene
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

    kontanktpersoner = [
        {"navn": "Nikolai", "stilling": "Sigma-sjef", "bilde": "nikolai.jpeg", "epost": "nikolai.kantine@yessirski.com", "tlf": "400 12 345"},
        {"navn": "Audun", "stilling": "Vaskehjelp", "bilde": "audun.jpeg", "epost": "audun.kantine@yessirski.com", "tlf": "401 23 456"},
        {"navn": "Ebbe", "stilling": "Lokal bidragsyter", "bilde": "ebbe.jpeg", "epost": "ebbe.kantine@yessirski.com", "tlf": "402 34 567"},
        {"navn": "Helene", "stilling": "Kasse", "bilde": "helene.jpeg", "epost": "helene.kantine@yessirski.com", "tlf": "403 45 678"},
        {"navn": "Ludvig", "stilling": "Assistent", "bilde": "ludvig.jpeg", "epost": "ludvig.kantine@yessirski.com", "tlf": "404 56 789"},
        {"navn": "Sebastian", "stilling": "kokk", "bilde": "sebastian.jpeg", "epost": "sebastian.kantine@yessirski.com", "tlf": "405 67 890"}
    ]


