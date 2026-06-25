import openpyxl
import io
from typing import List, Dict, Any

def generate_excel_report(intelligence_report: Dict[str, Any], businesses: List[Dict[str, Any]]) -> bytes:
    wb = openpyxl.Workbook()
    
    # Summary Sheet
    ws_summary = wb.active
    ws_summary.title = "Executive Summary"
    ws_summary.append(["BIRA - Market Intelligence Report"])
    ws_summary.append([])
    ws_summary.append(["Total Analyzed", intelligence_report.get("total_analyzed", 0)])
    ws_summary.append(["High Trust Count", intelligence_report.get("high_trust_count", 0)])
    ws_summary.append([])
    ws_summary.append(["Insights"])
    ws_summary.append([intelligence_report.get("market_insights", "")])
    
    # Businesses Sheet
    ws_biz = wb.create_sheet(title="Businesses")
    headers = ["Name", "Trust Score", "Security Score", "Fraud Risk", "Address", "Phone", "Website"]
    ws_biz.append(headers)
    
    for b in businesses:
        ws_biz.append([
            b.get("name", ""),
            b.get("trust_score", 0),
            b.get("security_score", 0),
            b.get("fraud_risk", ""),
            b.get("address", ""),
            b.get("phone", ""),
            b.get("website", "")
        ])
        
    buffer = io.BytesIO()
    wb.save(buffer)
    excel_bytes = buffer.getvalue()
    buffer.close()
    return excel_bytes
