from typing import TypedDict, List, Dict, Any, Optional

class ResearchState(TypedDict):
    search_id: int
    raw_query: str
    business_type: Optional[str]
    location: Optional[str]
    
    search_results: List[Dict[str, Any]]
    scraped_businesses: List[Dict[str, Any]]
    directory_results: List[Dict[str, Any]]
    reviews: List[Dict[str, Any]]
    social_profiles: List[Dict[str, Any]]
    
    verified_businesses: List[Dict[str, Any]]
    deduplicated_businesses: List[Dict[str, Any]]
    trust_scores: Dict[str, float]
    security_scores: Dict[str, float]
    
    intelligence_report: Optional[Dict[str, Any]]
    progress_messages: List[str]
    errors: List[str]
