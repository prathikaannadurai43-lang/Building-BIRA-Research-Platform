from duckduckgo_search import DDGS
from app.agents.state import ResearchState

async def search_web(state: ResearchState) -> ResearchState:
    state["progress_messages"].append("Searching web for businesses...")
    
    query = state["raw_query"]
    results = []
    
    try:
        with DDGS() as ddgs:
            # Simple DDG search as fallback or primary if Tavily not setup
            ddg_results = list(ddgs.text(query, max_results=10))
            for r in ddg_results:
                results.append({
                    "title": r.get("title"),
                    "url": r.get("href"),
                    "snippet": r.get("body"),
                    "source": "duckduckgo"
                })
    except Exception as e:
        state["errors"].append(f"Search failed: {e}")
        
    state["search_results"] = results
    state["progress_messages"].append(f"Found {len(results)} potential results.")
    return state
