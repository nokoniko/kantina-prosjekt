# Kantina-prosjekt

Dette er en <span style="color: #007bff;">Flask-basert</span> webapplikasjon for en kantine, designet for å presentere dagens meny, et fullstendig utvalg av varer, kontaktinformasjon for ansatte, og detaljerte beskrivelser av individuelle retter. Prosjektet legger vekt på <span style="color: #28a745;">bærekraft og kvalitet</span>.

## Funksjoner

-   **Dynamisk Dagsmeny**: Viser dagens rett basert på ukedagen.
-   **Omfattende Meny**: En dedikert side som viser alle hovedretter.
-   **Vareoversikt**: En side som lister opp ulike varer som drikke, snacks og andre matprodukter.
-   **Detaljerte Rettsider**: Hver hovedrett har sin egen side med beskrivelse og bilde.
-   **Kontaktinformasjon for Ansatte**: En kontaktside med detaljer (navn, stilling, e-post, telefon, bilde) for kantinepersonalet.
-   <span style="color: #28a745;">**Bærekraftsfokus**</span>: Fremhever kantinens forpliktelse til bærekraftige praksiser, som bruk av <span style="color: #28a745;">kortreiste råvarer</span> og reduksjon av matsvinn.
-   **Responsivt Design**: Tilpasser seg ulike skjermstørrelser for en god brukeropplevelse.

## Teknologier Brukt

-   **Python 3.x**
-   <span style="color: #007bff;">**Flask**</span>: Et lettvekts webrammeverk for Python.
-   <span style="color: #007bff;">**Jinja2**</span>: Templating-motor brukt av Flask for å generere HTML.
-   <span style="color: #007bff;">**HTML5**</span>
-   <span style="color: #007bff;">**CSS3**</span>

## Oppsett og Installasjon

Følg disse trinnene for å få prosjektet til å kjøre lokalt:

1.  **Klon repositoryet**:
    ```bash
    git clone https://github.com/nokoniko/kantina-prosjekt.git # Erstatt med den faktiske URL-en til ditt repository
    cd kantina-prosjekt
    ```

2.  **Opprett et virtuelt miljø**:
    Det er god praksis å bruke et virtuelt miljø for å håndtere prosjektavhengigheter.
    ```bash
    python3 -m venv venv
    source venv/bin/activate # På Windows bruk `venv\Scripts\activate`
    ```

3.  **Installer avhengigheter**:
    ```bash
    pip install Flask
    ```

4.  **Kjør applikasjonen**:
    ```bash
    python app.py # windowa
    python3 app.py # macOS/linux
    ```
    Applikasjonen vil vanligvis kjøre på `http://127.0.0.1:5000/`.

## Prosjektstruktur

```
kantina-prosjekt/
├── app.py                  # Hoved Flask-applikasjonsfil
├── static/                 # Statiske filer (CSS, bilder)
│   ├── css/
│   │   └── style.css       # Hovedstilark
│   └── img/                # Bilder for logoer, menyer, personer, etc.
├── templates/              # HTML-maler
│   ├── base.html           # Grunnmal for konsistent layout
│   ├── hjem/               # Hjemmeside-maler
│   │   └── index.html
│   ├── kantine/            # Kantine-spesifikke maler
│   │   ├── kontakt.html    # Kontaktside
│   │   ├── meny.html       # Full menyside
│   │   └── varer.html      # Vareside
│   └── retter/             # Detaljsider for individuelle retter
│       ├── andeconfit.html
│       ├── boeuf-bourguignon.html
│       ├── coq_au_vin.html
│       ├── hokkaido-suppe.html
│       └── ratatouille.html
└── utils/                  # Hjelpeskript
    ├── hjelp.py            # Hjelpefunksjoner (f.eks. logikk for dagsmeny)
    └── liste.py            # Datalagring for menyer, produkter, kontakter
```

## Bidrag

Du er velkommen til å forke repositoryet, gjøre forbedringer og sende inn pull requests.

## Lisens

Dette prosjektet er åpent kildekode og tilgjengelig under MIT-lisensen.

## Kilder

Chatgpt til å generere tekst til hjemmesiden og beskrivelsen til de forskjellige rettene.
