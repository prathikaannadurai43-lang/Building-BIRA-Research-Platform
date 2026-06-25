from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import io
from typing import List, Dict, Any

def generate_pdf_report(intelligence_report: Dict[str, Any], businesses: List[Dict[str, Any]]) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    elements.append(Paragraph("BIRA - Executive Intelligence Report", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Insights
    elements.append(Paragraph("Market Insights", styles['Heading2']))
    insights = intelligence_report.get("market_insights", "No insights generated.")
    elements.append(Paragraph(insights, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Top Businesses Table
    elements.append(Paragraph("Top Trusted Businesses", styles['Heading2']))
    
    data = [["Name", "Trust Score", "Security", "Fraud Risk"]]
    for b in businesses[:10]: # Top 10
        data.append([
            b.get("name", "N/A"),
            str(b.get("trust_score", 0)),
            str(b.get("security_score", 0)),
            b.get("fraud_risk", "Unknown")
        ])
        
    t = Table(data, colWidths=[200, 80, 80, 80])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    
    elements.append(t)
    doc.build(elements)
    
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
