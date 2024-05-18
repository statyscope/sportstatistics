import scripts.config

table_cols = ['Lag',
            'Tabellplacering, Poäng, Målskillnad', 
            'Hemma/borta resultat, målskillnad',
            'Form senaste 5 matcherna',
            'Saknade nyckelspelare',
            'Tränare',
            'Head to head senaste 3 ggr',
            'Matcher som spelats senaste 7 dagarna',
            'Övriga kommentarer']


leagues = {
    'Premier League': [
        'Arsenal',
        'Liverpool',
        'Manchester City',
        'Tottenham Hotspur',
        'Aston Villa',
        'Manchester United',
        'West Ham',
        'Newcastle',
        'Chelsea',
        'Brighton & Hove Albion',
        'Wolves',
        'AFC Bournemouth',
        'Fulham',
        'Crystal Palace',
        'Brentford',
        'Everton',
        'Nottingham Forest',
        'Luton Town',
        'Burnley',
        'Sheffield United',
    ],
    'Championship': list(scripts.config.CHAMPIONSHIP_SLUG.keys()),
    "LaLiga EA Sports": list(scripts.config.PRIMERA_DIVISION_SLUG.keys()), 
    "Serie A": list(scripts.config.SERIE_A_SLUG.keys()),
    "Bundesliga": list(scripts.config.BUNDESLIGA_SLUG.keys()),
    "Ligue 1": list(scripts.config.LIGUE_1_SLUG.keys()),
    "Allsvenskan": list(scripts.config.ALLSVENSKAN_SLUG.keys()),
    "Eliteserien": list(scripts.config.ELITESERIEN_SLUG.keys()),
}