from typing import List, Dict, Any
from app.agents.llm import call_llm

async def generate_intelligence(businesses: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generates an intelligence report based on the collected business data.
    """
    if not businesses:
        return {"error": "No businesses to analyze"}
        
    total = len(businesses)
    high_trust = sum(1 for b in businesses if b.get("trust_score", 0) > 80)
    
    # Generate summary with LLM
    names = [b.get("name", "Unknown") for b in businesses]
    
    prompt = f"Analyze this list of businesses and provide a short market insight summary. Businesses: {names}"
    system_prompt = "You are a business intelligence analyst. Provide a 2-3 sentence market summary."
    
    insight_text = await call_llm(prompt, system_prompt)
    
    return {
        "total_analyzed": total,
        "high_trust_count": high_trust,
        "market_insights": insight_text,
        "top_businesses": sorted(businesses, key=lambda x: x.get("trust_score", 0), reverse=True)[:5]
    }
