# mcp-blog

This repository contains a collection of MCP (Model Control Protocol) server implementations and configuration files related to this blog post: https://www.tenable.com/blog

## Files Overview

### Python Files

- **tenable_mcp_blog.py**: Tools discussed in the blog:
  - `log_pwd()`: Returns the path to the log file
  - `log_mcp_tool_usage()`: Logs MCP tool usage
  - `filter_mcp_tool_usage()`: Filters and controls tool access like a firewall
  - `filter_and_analyze_llm_system_prompt()`: Analyzes system prompts

- **mcp_framework.py**: Base framework template for creating MCP servers, includes:
  - Basic MCP server setup
  - Example tool implementation structure (`mcp_tool_name()`)
  - Support for both stdio and SSE transport

- **hidden_mcp_finder.py**: Utility MCP server that logs and tracks other inline tools and MCP tool usage.
  - `log_other_inline_tools()`: Logs and monitors other MCP tools being used

### Configuration Files

- **claude_desktop_config.json**: Sample configuration file for Claude Desktop

### Logs

- **testlog.log**: Example log file from the system prompt examples

## Environment Setup

The project uses Python with the following dependencies:
- FastMCP
- python-dotenv
- typing

To get started, ensure you have Python installed. Create a venv and install the required libraries. I didn't create a requirements.txt for this.