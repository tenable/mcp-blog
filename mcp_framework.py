from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Initialize FastMCP server
mcp = FastMCP("Tenable MCP Security", "1.0")

# Load environment variables from .env file if present
load_dotenv()

# < TOOLS GO HERE >
@mcp.tool()
async def mcp_tool_name(tool_param_1: str, tool_param_2: str) -> str:
    """This text is the tool's description and is sent to the LLM when a session is started.
    
    It can also indicate the return value.
    """
    print("Hello World!") # This is the body of the MCP tool. Do something!

    return f"And, of course, we return something to the LLM at the end. This could be dynamic or could be JSON, whatever you think the LLM can handle."

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
    # mcp.run(transport='sse')
