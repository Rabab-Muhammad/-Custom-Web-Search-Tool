import requests
from decouple import config

# Load API key from .env
TAVILY_API_KEY = config("TAVILY_API_KEY")

def tavily_search(query: str, search_depth: str = "basic"):
    """
    Tavily API ko call karke results return karega
    """
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": search_depth
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["results"]
    else:
        return {"error": "Request failed", "status": response.status_code}
