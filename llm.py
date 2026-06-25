from openai import AsyncOpenAI
import json
from app.config import settings

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY,
)

# Use free models
DEFAULT_MODEL = "qwen/qwen-2.5-7b-instruct:free"

async def call_llm(prompt: str, system_prompt: str = "You are a helpful AI.", response_format=None) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    
    kwargs = {
        "model": DEFAULT_MODEL,
        "messages": messages,
        "temperature": 0.1,
    }
    
    if response_format:
        # Some free models may not fully support structured outputs, 
        # but we pass it if provided, or we can prompt for JSON.
        kwargs["response_format"] = {"type": "json_object"}
        messages[0]["content"] += "\nRespond ONLY with valid JSON."
        
    try:
        response = await client.chat.completions.create(**kwargs)
        return response.choices[0].message.content
    except Exception as e:
        print(f"LLM Error: {e}")
        return "{}" if response_format else ""
