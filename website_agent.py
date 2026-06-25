from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from app.agents.state import ResearchState
from app.agents.llm import call_llm
import json

async def scrape_website(url: str) -> str:
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle", timeout=15000)
            html = await page.content()
            await browser.close()
            
            soup = BeautifulSoup(html, "html.parser")
            # Remove scripts and styles
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text(separator="\n")
            return text[:5000] # Limit to 5000 chars for LLM context
    except Exception as e:
        print(f"Scraping error: {e}")
        return ""

async def extract_business_info(state: ResearchState) -> ResearchState:
    state["progress_messages"].append("Scraping business websites...")
    
    scraped = []
    # Limit to top 3 results to save time
    top_urls = [r["url"] for r in state.get("search_results", [])[:3] if "http" in r["url"]]
    
    for url in top_urls:
        state["progress_messages"].append(f"Scraping {url}...")
        text = await scrape_website(url)
        if not text:
            continue
            
        prompt = f"Extract business info from this text. Keys: name, address, phone, email. Text: {text}"
        sys = "Extract business details into JSON."
        resp = await call_llm(prompt, sys, response_format=True)
        
        try:
            data = json.loads(resp)
            data["website"] = url
            data["source"] = "website_scrape"
            scraped.append(data)
        except:
            pass

    state["scraped_businesses"] = scraped
    return state
