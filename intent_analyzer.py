import json
from app.agents.state import ResearchState
from app.agents.llm import call_llm

async def analyze_intent(state: ResearchState) -> ResearchState:
    query = state["raw_query"]
    state["progress_messages"].append(f"Analyzing intent for: {query}")
    
    prompt = f"Extract the business type and location from this query: '{query}'"
    sys_prompt = "You extract business types and locations. Output JSON keys: 'business_type', 'location'. If missing, use null."
    
    response = await call_llm(prompt, sys_prompt, response_format=True)
    
    try:
        data = json.loads(response)
        state["business_type"] = data.get("business_type")
        state["location"] = data.get("location")
        state["progress_messages"].append(f"Found: {state['business_type']} in {state['location']}")
    except Exception:
        state["errors"].append("Failed to parse intent")
        
    return state
