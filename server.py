import os 
import httpx
from mcp.server.fastmcp import FastMCP
mcp= FastMCP("weather server")
API_KEY= os.getenv("OPENWEATHER_API_KEY")

@mcp.tool()
async def get_weather(city: str) -> dict:
"""Get current weather for a city"""
url="https://api.openweathermap.org/data/2.5/weather"
params ={
    "q" : city,
    "appid":API_KEY,
    "units":"metric"
    }
    
    async with httpx.ASynclient() as client:
    res = await client.get(url,params = params)
    data = res.json()
    
    return{
        "city":city,
        "temperature":data["main"]["temp"],
        "description":data["weather"][0]["description"]
        }
        
        
    