import csv
import io
from typing import List, Dict, Any

def generate_csv_report(businesses: List[Dict[str, Any]]) -> str:
    output = io.StringIO()
    if not businesses:
        return ""
        
    headers = ["name", "trust_score", "security_score", "fraud_risk", "address", "phone", "website", "is_verified"]
    writer = csv.DictWriter(output, fieldnames=headers, extrasaction='ignore')
    
    writer.writeheader()
    for b in businesses:
        writer.writerow(b)
        
    return output.getvalue()
