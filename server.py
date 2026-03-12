 
from mcp.server.fastmcp import FastMCP
from weather import get_weather as weather_tool

mcp= FastMCP("weather server")


@mcp.tool()
async def get_weather(city: str) -> dict:
    """Get current weather for a city"""
    return await weather_tool(city)  
        
if __name__ == "__main__":
    mcp.run()
