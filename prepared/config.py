import requests
from bs4 import BeautifulSoup

def extract_initial_configurations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    initial_configurations = []
    for pattern in soup.find_all('a', class_='pattern'):
        name = pattern['name']
        url = pattern['href']

        initial_configuration = requests.get(url).content
        initial_configurations.append((name, initial_configuration))

    return initial_configurations

if __name__ == '__main__':
    url = 'https://www.conwaylife.com/patterns/'
    initial_configurations = extract_initial_configurations(url)

    for name, initial_configuration in initial_configurations:
        with open(f'conwaylife/{name}.txt', 'wb') as f:
            f.write(initial_configuration)