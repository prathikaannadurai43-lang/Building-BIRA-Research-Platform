import httpx
from typing import Dict, Any

async def check_website_security(url: str) -> Dict[str, Any]:
    """
    Checks HTTPS/SSL validity and generates a security score.
    """
    if not url:
        return {"security_score": 0, "https_enabled": False}
        
    if not url.startswith("http"):
        url = "https://" + url
        
    try:
        async with httpx.AsyncClient(verify=True, timeout=5.0) as client:
            response = await client.get(url)
            
        # If we reached here, SSL verification passed and it responded.
        return {
            "security_score": 100 if url.startswith("https") else 50,
            "https_enabled": url.startswith("https"),
            "status_code": response.status_code
        }
    except httpx.ConnectTimeout:
        return {"security_score": 20, "https_enabled": False, "error": "timeout"}
    except httpx.ConnectError:
        return {"security_score": 10, "https_enabled": False, "error": "connection failed"}
    except Exception as e:
        return {"security_score": 0, "https_enabled": False, "error": str(e)}

async def run_security_checks(businesses: list[Dict[str, Any]]) -> list[Dict[str, Any]]:
    for biz in businesses:
        if biz.get("website"):
            security_data = await check_website_security(biz["website"])
            biz["security_score"] = security_data.get("security_score", 0)
        else:
            biz["security_score"] = 0
    return businesses
