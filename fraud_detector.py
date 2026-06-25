from typing import Dict, Any

def detect_fraud_risk(business: Dict[str, Any]) -> str:
    """
    Detects fraud risk (Low, Medium, High) based on missing information.
    """
    missing_points = 0
    
    if not business.get("website"):
        missing_points += 2
        
    if not business.get("phone"):
        missing_points += 2
        
    if not business.get("address"):
        missing_points += 1
        
    if business.get("trust_score", 0) < 30:
        missing_points += 3
        
    if missing_points >= 5:
        return "High"
    elif missing_points >= 3:
        return "Medium"
    return "Low"

def evaluate_fraud_risks(businesses: list[Dict[str, Any]]) -> list[Dict[str, Any]]:
    for biz in businesses:
        biz["fraud_risk"] = detect_fraud_risk(biz)
    return businesses
