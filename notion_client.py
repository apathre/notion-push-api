import requests

NOTION_API_BASE_URL = "https://api.notion.com/v1/"
NOTION_API_KEY ="notion_secret_8Ohy6v8BeZQj3zMyg6F9qr1gOLImmqPEOxavtFMOTnI11"
database_id ="be5f88cb25ab447cb153c46f2d87aa04"


headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-version": "2022-06-28"

}

def fetch_from_notion(endpoint: str):
    response = requests.get(f"{NOTION_API_BASE_URL}{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()

def post_to_notion(endpoint: str, data: dict):
    response = requests.post(f"{NOTION_API_BASE_URL}{endpoint}", headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def patch_to_notion(endpoint: str, data: dict):
    response = requests.patch(f"{NOTION_API_BASE_URL}{endpoint}", headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def put_to_notion(endpoint: str, data: dict):
    url = f"{NOTION_API_BASE_URL}{endpoint}"
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
