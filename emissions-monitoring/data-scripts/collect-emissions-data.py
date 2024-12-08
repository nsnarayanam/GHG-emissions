import requests

def fetch_emissions_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(f"Fetched {len(data)} records.")
        return data
    else:
        print("Failed to fetch data.")
        return None

fetch_emissions_data("https://api.example.com/emissions")
