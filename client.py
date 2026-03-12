import asyncio 
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command = "python",
        args = ["server.py"]
    )

    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read, write) as session:
                await session.initialize()

                result = await session.call_tool(
                    "get_weather",
                    {"city":"Amsterdam"}
                )

                print(result)


asyncio.run(main())