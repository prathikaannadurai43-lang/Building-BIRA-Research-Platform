from langgraph.graph import StateGraph, END
from app.agents.state import ResearchState
from app.agents.intent_analyzer import analyze_intent
from app.agents.search_agent import search_web
from app.agents.website_agent import extract_business_info

def build_workflow():
    workflow = StateGraph(ResearchState)
    
    workflow.add_node("intent", analyze_intent)
    workflow.add_node("search", search_web)
    workflow.add_node("scrape", extract_business_info)
    
    workflow.add_edge("intent", "search")
    workflow.add_edge("search", "scrape")
    workflow.add_edge("scrape", END)
    
    workflow.set_entry_point("intent")
    
    return workflow.compile()

research_workflow = build_workflow()
