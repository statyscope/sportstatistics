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
    "Allsvenskan": "allsvenskan",
    "Eliteserien": "eliteserien",  
}

PREMIER_LEAGUE_SLUG = {
    'Arsenal': 'arsenal',
    'Liverpool': 'liverpool',
    'Manchester City': 'manchester-city-fc',
    'Tottenham Hotspur': 'tottenham-hotspur-fc',
    'Tottenham': 'tottenham-hotspur-fc',
    'Aston Villa': 'aston-villa-fc',
    'Manchester United': 'manchester-united-fc',
    'West Ham': 'west-ham-united',
    'Newcastle': 'newcastle-united-fc',
    'Brighton & Hove Albion': 'brighton-amp-hov',
    'Brighton': 'brighton-amp-hov',
    'Wolves': 'wolverhampton',
    'Wolverhampton': 'wolverhampton',
    'AFC Bournemouth': 'afc-bournemouth',
    'Chelsea': 'chelsea-fc',
    'Fulham': 'fulham',
    'Crystal Palace': 'crystal-palace-fc',
    'Brentford': 'brentford',
    'Everton': 'everton-fc',
    'Nottingham Forest': 'nottingham-forest-fc',
    'Luton Town': 'luton-town-fc',
    'Burnley': 'burnley-fc',
    'Sheffield United': 'sheffield-united',
}

CHAMPIONSHIP_SLUG = {
    'Leicester': 'leicester-city-fc',
    'Leeds United': 'leeds-united-afc',
    'Ipswich Town': 'ipswich-town-fc',
    'Southampton': 'southampton-fc',
    'West Bromwich Albion': 'west-bromwich',
    'Norwich City': 'norwich-city-fc',
    'Hull City': 'hull-city',
    'Coventry City': 'coventry-city',
    'Middlesbrough': 'middlesbrough-fc',
    'Preston North End': 'preston-north-end',
    'Cardiff City': 'cardiff-city-fc',
    'Bristol City': 'bristol-city-fc',
    'Sunderland': 'sunderland-afc',
    'Swansea City': 'swansea-city-afc',
    'Watford': 'watford-fc',
    'Millwall': 'millwall-fc',
    'Stoke City': 'stoke-city',
    'Queens Park Rangers': 'queens-park-rangers-fc',
    'Blackburn Rovers': 'blackburn-rovers-fc',
    'Plymouth Argyle': 'plymouth-argyle',
    'Sheffield Wednesday': 'sheffield-wednesday-fc',
    'Birmingham City': 'birmingham-city-fc',
    'Huddersfield Town': 'huddersfield-town-fc',
    'Rotherham United': 'rotherham-united', 
}

PRIMERA_DIVISION_SLUG = {
    "Athletic": "athletic-bilbao",
    "Atlético": "atletico-madrid",
    "Sevilla": "sevilla",
    "Villarreal": "villarreal",
}

SERIE_A_SLUG = {
    "Atalanta": "atalanta",
    "Bologna": "bologna",
    "Napoli": "napoli",
}

BUNDESLIGA_SLUG = {
    "B. Dortmund": "borussia-dortmund",
    "Mainz 05": "mainz-amat",
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
    "Molde FK": "molde-fk",
    "Rosenborg BK": "rosenborg-bk",
}


ALL_TEAMS_SLUG = {**PREMIER_LEAGUE_SLUG, **CHAMPIONSHIP_SLUG, **PRIMERA_DIVISION_SLUG, **SERIE_A_SLUG, **BUNDESLIGA_SLUG, **ALLSVENSKAN_SLUG, **ELITESERIEN_SLUG}