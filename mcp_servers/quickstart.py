"""
Awesome MCP Toolkit - Quickstart MCP Server
A minimal Python MCP Server built with FastMCP.
"""

from fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("Awesome MCP Toolkit Starter")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def search_toolkit_docs(query: str) -> str:
    """Search documentation within Awesome MCP Toolkit."""
    return f"Search results for '{query}' in Awesome MCP Toolkit."

if __name__ == "__main__":
    mcp.run()
