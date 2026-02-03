import requests

def fetch_data(endpoint, filters=None):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters)

    if response.status_code == 200:
        return response.json()
    return None

characters = fetch_data("character", {"name": "Rick"})

if characters:
    for c in characters.get("results", [])[:10]:
        print(f"{c['id']:>3} | {c['name']} | {c['status']} | {c['species']}")
else:
    print("Failed to fetch data")
