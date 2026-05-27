# math_server.py
import logging
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

# Configure a logger
logger = logging.getLogger("math_mcp_server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    logger.info(f"Running add tool with a={a}, b={b}")
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    logger.info(f"Running multiply tool with a={a}, b={b}")
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")