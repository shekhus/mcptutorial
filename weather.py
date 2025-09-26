from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_current_weather(location: str) -> str:
    """Get the current weather in a given location."""
    # Dummy implementation for illustration purposes
    return f"The current weather in {location} is sunny with a temperature of 25°C."