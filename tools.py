from agents import function_tool
from tavily_api import tavily_search

@function_tool
def web_search(query: str) -> str:
    """
    Tavily API se search karke top 5 results return karega
    """
    results = tavily_search(query)
    if "error" in results:
        return "Error fetching results"

    formatted = "\n".join(
        [f"{i+1}. {r['title']} ({r['url']})" for i, r in enumerate(results[:5])]
    )
    return formatted
