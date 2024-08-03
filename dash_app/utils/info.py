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
        'AFC Bournemouth',
        'Arsenal',
        'Aston Villa',
        'Brentford',
        'Brighton & Hove Albion',
        'Chelsea',
        'Crystal Palace',
        'Everton',
        'Fulham',
        'Ipswich Town',
        'Leicester',
        'Liverpool',
        'Manchester City',
        'Manchester United',
        'Newcastle',
        'Nottingham Forest',
        'Southampton',
        'Tottenham Hotspur',   
        'West Ham',
        'Wolves',
    ],
    'Championship': list(scripts.config.CHAMPIONSHIP_SLUG.keys()),
    "LaLiga EA Sports": list(scripts.config.PRIMERA_DIVISION_SLUG.keys()), 
    "Serie A": list(scripts.config.SERIE_A_SLUG.keys()),
    "Bundesliga": list(scripts.config.BUNDESLIGA_SLUG.keys()),
    "Ligue 1": list(scripts.config.LIGUE_1_SLUG.keys()),
    "Allsvenskan": list(scripts.config.ALLSVENSKAN_SLUG.keys()),
    "Eliteserien": list(scripts.config.ELITESERIEN_SLUG.keys()),
}