import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# URLs
TOTAL_URL = os.getenv("TOTAL_URL")
HOME_URL = os.getenv("HOME_URL")
AWAY_URL = os.getenv("AWAY_URL")

LEAGUE_URL = os.getenv("LEAGUE_URL")
PREMIER_LEAGUE_URL = os.getenv("PREMIER_LEAGUE_URL")
TEAM_URL = os.getenv("TEAM_URL")

# The old versions of Besoccer navigation
# Use if the new one fails
LEAGUE_URL_OLD = os.getenv("LEAGUE_URL_OLD")
PREMIER_LEAGUE_URL_OLD = os.getenv("PREMIER_LEAGUE_URL_OLD")

HEADERS = {
    'accept': '*/*',
    'accept-language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,nb;q=0.5',
    # 'cache-control': 'max-age=0',
    # 'if-none-match': 'W/"977d929fd0"',
    'origin': os.getenv("HEADERS_URL"),
    'referer': os.getenv("HEADERS_URL"),
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

# Slug

LEAGUE_SLUG = {
    'Premier League': 'premier_league',
    'Championship': 'championship',
    "LaLiga EA Sports": "primera_division",
    "Serie A": "serie_a",
    "Bundesliga": "bundesliga",
    "Ligue 1": "ligue_1",
    "Allsvenskan": "allsvenskan",
    "Eliteserien": "eliteserien",
}

PREMIER_LEAGUE_SLUG = {
    'AFC Bournemouth': 'afc-bournemouth',
    'Arsenal': 'arsenal',
    'Aston Villa': 'aston-villa-fc',
    'Brentford': 'brentford',
    'Brighton & Hove Albion': 'brighton-amp-hov',
    'Chelsea': 'chelsea-fc',
    'Crystal Palace': 'crystal-palace-fc',
    'Everton': 'everton-fc',
    'Fulham': 'fulham',
    'Ipswich Town': 'ipswich-town-fc',
    'Leicester': 'leicester-city-fc',
    'Liverpool': 'liverpool',
    'Manchester City': 'manchester-city-fc',
    'Manchester United': 'manchester-united-fc',
    'Newcastle': 'newcastle-united-fc',
    'Nottingham Forest': 'nottingham-forest-fc',
    'Southampton': 'southampton-fc',
    'Tottenham Hotspur': 'tottenham-hotspur-fc',
    'West Ham': 'west-ham-united',
    'Wolves': 'wolverhampton',
}

CHAMPIONSHIP_SLUG = {
    'Blackburn Rovers': 'blackburn-rovers-fc',
    'Bristol City': 'bristol-city-fc',
    'Burnley': 'burnley-fc',
    'Cardiff City': 'cardiff-city-fc',
    'Coventry City': 'coventry-city',
    'Derby County': 'derby-county-fc',
    'Hull City': 'hull-city',
    'Leeds United': 'leeds-united-afc',
    'Luton Town': 'luton-town-fc',
    'Middlesbrough': 'middlesbrough-fc',
    'Millwall': 'millwall-fc',
    'Norwich City': 'norwich-city-fc',
    'Oxford United': 'oxford-united',
    'Plymouth Argyle': 'plymouth-argyle',
    'Portsmouth': 'portsmouth',
    'Preston North End': 'preston-north-end',
    'Queens Park Rangers': 'queens-park-rangers-fc',
    'Sheffield United': 'sheffield-united',
    'Sheffield Wednesday': 'sheffield-wednesday-fc',
    'Stoke City': 'stoke-city',
    'Sunderland': 'sunderland-afc',
    'Swansea City': 'swansea-city-afc',
    'Watford': 'watford-fc',
    'West Bromwich Albion': 'west-bromwich',
}

PRIMERA_DIVISION_SLUG = {
    "Athletic": "athletic-bilbao",
    "Atlético": "atletico-madrid",
    "Barcelona": "barcelona",
    "Celta": "celta",
    "Deportivo Alavés": "alaves",
    "Espanyol": "espanyol",
    "Getafe": "getafe",
    "Girona": "girona-fc",
    "Las Palmas": "ud-palmas",
    "Leganés": "leganes",
    "Mallorca": "mallorca",
    "Osasuna": "osasuna",
    "Rayo Vallecano": "rayo-vallecano",
    "Real Betis": "betis",
    "Real Madrid": "real-madrid",
    "Real Sociedad": "real-sociedad",
    "Real Valladolid": "valladolid",
    "Sevilla": "sevilla",
    "Valencia": "valencia-cf",
    "Villarreal": "villarreal",
}

SERIE_A_SLUG = {
    "AC Monza": "ac-monza-brianza-1912",
    "Atalanta": "atalanta",
    "Bologna": "bologna",
    "Cagliari": "cagliari",
    "Como": "como",
    "Empoli": "empoli-fc",
    "Fiorentina": "fiorentina",
    "Genoa": "genoa",
    "Hellas Verona": "hellas-verona-fc",
    "Inter": "internazionale",
    "Juventus": "juventus-fc",
    "Lazio": "lazio",
    "Lecce": "lecce",
    "Milan": "milan",
    "Napoli": "napoli",
    "Parma": "parma-fc",
    "Roma": "roma",
    "Torino": "torino-fc",
    "Udinese": "udinese",
    "Venezia": "venezia",
}

BUNDESLIGA_SLUG = {
    "FC Augsburg": "fc-augsburg",
    "B. Dortmund": "borussia-dortmund",
    "B. Leverkusen": "bayer-leverkusen",
    "B. Mönchengladbach": "borussia-monchengla",
    "Bayern München": "bayern-munchen",
    "Eintracht Frankfurt": "eintracht-frankfurt",
    "SC Freiburg": "sc-freiburg",
    "Heidenheim": "heidenheim",
    "Hoffenheim": "tsg-1899-hoffenheim",
    "Holstein Kiel": "holstein-kiel",
    "RB Leipzig": "rb-leipzig",
    "Mainz 05": "mainz-amat",
    "FC St Pauli": "st-pauli",
    "Stuttgart": "stuttgart",
    "Union Berlin": "1-fc-union-berlin",
    "VfL Bochum": "bochum",
    "Werder Bremen": "werder-bremen",
    "Wolfsburg": "wolfsburg",
}

LIGUE_1_SLUG = {
    "Angers SCO": "angers-sco",
    "Auxerre": "auxerre",
    "Le Havre": "havre-ac",
    "Lens": "lens",
    "Lille": "lillestrom",
    "Monaco": "monaco",
    "Montpellier": "montpellier",
    "Nantes": "nantes",
    "Nice": "nice",
    "Olympique Lyonnais": "olympique-lyonnais",
    "Olympique Marseille": "olympique-marsella",
    "PSG": "paris-saint-germain-fc",
    "Saint-Étienne": "saint-etienne",
    "Stade Brestois": "stade-brestois-29",
    "Stade de Reims": "stade-reims",
    "Stade Rennais": "stade-rennes",
    "Strasbourg": "strasbourg",
    "Toulouse": "toulouse-fc",
}

ALLSVENSKAN_SLUG = {
    "AIK Solna": "aik-solna",
    "Brommapojkarna": "brommapojkarna",
    "Djurgårdens IF": "djurgardens-if",
    "IF Elfsborg": "if-elfsborg-boras",
    "GAIS": "gais-goteborg",
    "IFK Göteborg": "ifk-goteborg",
    "Halmstads": "halmstads-bk",
    "Hammarby IF": "hammarby-if",
    "Häcken": "hacken",
    "Kalmar FF": "kalmar-ff",
    "Malmö FF": "malmo-ff",
    "Mjällby AIF": "mjallby",
    "IFK Norrköping": "ifk-norrkoping",
    "IK Sirius": "sirius",
    "IFK Varnamo": "ifk-varnamo",
    "Västerås SK": "vasteras-sk",
}

ELITESERIEN_SLUG = {
    "FK Bodo Glimt": "fk-bodo-glimt",
    "SK Brann": "sk-brann-bergen",
    "Fredrikstad": "fredrikstad-fk",
    "HamKam": "hamkam",
    "Haugesund": "haugesund",
    "KFUM Oslo": "kfum",
    "Kristiansund BK": "kristiansund-bk",
    "Lillestrom SK": "lillestrom-sk",
    "Molde FK": "molde-fk",
    "Odd": "odd-grenland-skien",
    "Rosenborg BK": "rosenborg-bk",
    "Sandefjord": "sandefjord-fotball",
    "Sarpsborg 08": "sarpsborg-08",
    "Stromsgodset IF": "stromsgodset-if",
    "Tromsø IL": "tromso",
    "Viking Stavanger": "viking-stavanger",
}


ALL_TEAMS_SLUG = {
    **PREMIER_LEAGUE_SLUG,
    **CHAMPIONSHIP_SLUG,
    **PRIMERA_DIVISION_SLUG,
    **SERIE_A_SLUG,
    **BUNDESLIGA_SLUG,
    **LIGUE_1_SLUG,
    **ALLSVENSKAN_SLUG,
    **ELITESERIEN_SLUG
}
