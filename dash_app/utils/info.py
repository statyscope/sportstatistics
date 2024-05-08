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
    "Allsvenskan": list(scripts.config.ALLSVENSKAN_SLUG.keys()),
}