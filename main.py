import requests

TOKEN = '2619421814940190' 


urls = [f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk', f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos', f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',] 

def requests_get(url_all):
    
    result = (requests.get(url) for url in url_all)
    return result

def structuring():

    creature = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                creature.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in creature:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")


structuring()