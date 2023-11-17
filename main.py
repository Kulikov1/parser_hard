import requests

from constans import QUERY, STORES

if __name__ == '__main__':
    for store in STORES:
        r = requests.post(
            'https://api.metro-cc.ru/products-api/graph',
            json={"query": QUERY % STORES[store]}
        )
        with open(f"result_{store}.json", 'w', encoding="utf-8") as file:
            file.write(r.text)
