import requests
import json
from bs4 import BeautifulSoup


def main():
    # while True:
    query = requests.get('https://github.com/skrabik/MathMode2024/watchers')
    # print(query.text)
    soup = BeautifulSoup(query.text, features="html.parser")
    div = soup.find_all('li', {'class': 'col-md-4 mb-3'})
    div = str(div[0])
    print(len(div))


if __name__ == '__main__':
    main()