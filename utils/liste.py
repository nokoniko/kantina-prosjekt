class Liste:
    def __init__(self, name) -> None:
        self.name = name

    # lagger 2 lister den enne til mat menyen og den adnre til de faste varerene
    menyen = [
        {"navn": "Andeconfit", "kategori": "Varmrett", "allergier": ["gluten", "melk"], "bilde": "andeconfit.jpeg", "dag": "Mandag", "slug": "andeconfit"},
        {"navn": "Coq au vin", "kategori": "Varmrett", "allergier": [], "bilde": "coq_au_vin.jpg", "dag": "Tirsdag", "slug": "coq_au_vin"},
        {"navn": "Hokkaido-suppe", "kategori": "Suppe", "allergier": ["melk"], "bilde": "hokkaido_suppe.jpeg", "dag": "Onsdag", "slug": "hokkaido-suppe"},
        {"navn": "Bœuf bourguignon", "kategori": "Varmrett", "allergier": [], "bilde": "boeuf_bourguignon.jpg", "dag": "Torsdag", "slug": "boeuf-bourguignon"},
        {"navn": "Ratatouille", "kategori": "Vegetarrett", "allergier": [], "bilde": "ratatouille.jpg", "dag": "Fredag", "slug": "ratatouille"}
    ]

    varere = [
        {"navn": "Sjokolademelk", "kategori": "Drikke", "allergier": ["melk"], "bilde": "sjokolademelk.jpeg", "pris": 68},
        {"navn": "Eplejuice", "kategori": "Drikke", "allergier": [], "bilde": "epplejuice.jpg", "pris": 62},
        {"navn": "Mineralvann", "kategori": "Drikke", "allergier": [], "bilde": "vann.jpg", "pris": 52},
        {"navn": "Nøtteblanding", "kategori": "Snack", "allergier": ["nøtter"], "bilde": "notter.jpg", "pris": 42},
        {"navn": "Yoghurt med granola", "kategori": "Snack", "allergier": ["melk", "gluten", "nøtter"], "bilde": "yoghurt.jpeg", "pris": 58},
        {"navn": "Croissant", "kategori": "Bakverk", "allergier": ["gluten", "melk"], "bilde": "Croissant.jpg", "pris": 50},
        {"navn": "Baguette med ost og skinke", "kategori": "Mat", "allergier": ["gluten", "melk"], "bilde": "bagguete.jpg", "pris": 100},
        {"navn": "Salatboks", "kategori": "Mat", "allergier": ["egg"], "bilde": "salat.Jpeg", "pris":120},
        {"navn": "Fruktbeger", "kategori": "Snack", "allergier": [], "bilde": "fruktBeger.jpg", "pris": 90},
        {"navn": "Kaffe", "kategori": "Drikke", "allergier": [], "bilde": "kaffe.jpg", "pris": 33},
        {"navn": "Te", "kategori": "Drikke", "allergier": [], "bilde": "te.png", "pris": 33},
        {"navn": "Brownie", "kategori": "Bakverk", "allergier": ["gluten", "melk", "egg"], "bilde": "brownie.webp", "pris": 67}
    ]

    kontanktpersoner = [
        {"navn": "Nikolai pai", "stilling": "Sigma-sjef", "bilde": "nikolai.jpeg", "epost": "nikolai.kantine@yessirski.com", "tlf": "400 12 345"},
        {"navn": "Audun bao bum", "stilling": "Vaskehjelp", "bilde": "audun.jpeg", "epost": "audun.kantine@yessirski.com", "tlf": "401 23 456"},
        {"navn": "Ebbe Lebbe", "stilling": "Lokal narkoman", "bilde": "ebbe.jpg", "epost": "ebbe.kantine@yessirski.com", "tlf": "402 34 567"},
        {"navn": "Helene grene", "stilling": "Kasen", "bilde": "helene.jpeg", "epost": "helene.kantine@yessirski.com", "tlf": "403 45 678"},
        {"navn": "Ludvig sudvig", "stilling": "Marketing sjeff", "bilde": "ludvig.jpeg", "epost": "ludvig.kantine@yessirski.com", "tlf": "404 56 789"},
        {"navn": "Sebastian nastian", "stilling": "kokk", "bilde": "sebastian.jpeg", "epost": "sebastian.kantine@yessirski.com", "tlf": "405 67 890"},
        {"navn": "markus", "stilling": "alkaholiker", "bilde": "markus2.jpg", "epost": "markus.kantine@yessirski.com", "tlf": "406 41 911"},
        {"navn": "thea", "stilling": "Die Fürer", "bilde": "thea.jpg", "epost": "thea.kantine@yessirski.com", "tlf": "407 44 671"}
    ]