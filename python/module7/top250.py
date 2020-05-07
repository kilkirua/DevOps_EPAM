import json
import requests
from bs4 import BeautifulSoup

def parse_top_250(file_name):
    request = requests.get('https://imdb.com/chart/top',
                           headers={'Accept-Language': 'En-us'})
    soup = BeautifulSoup(request.text, 'lxml')
    top250 = []
    for tr in soup.tbody.find_all('tr'):
        title = tr.find('td', class_='titleColumn').a.text
        position = tr.find('td', class_='posterColumn').span['data-value']
        year = tr.find('td', class_='titleColumn').span.text.strip('()')
        crew = tr.find('td', class_='titleColumn').a['title'].split(', ')
        rating = tr.find('td', class_='ratingColumn imdbRating').strong.text
        info = {title: {'Position': position,
                        'Year': year,
                        'Director': crew[0].strip(' (dir.)'),
                        'Crew': f"{crew[1]}, {crew[2]}",
                        'Rating': rating,
                        }
                }
        top250.append(info)
    with open(file_name, 'w') as f_write:
        f_write.write(json.dumps(top250))
