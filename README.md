
# MCP Server for Interacting with Yahoo Finance #

---

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open standard developed by Anthropic to enable seamless integration between Large Language Models (LLMs) and external tools, services, and data sources.

This project provides a simple implementation that allows LLM to interact with Yahoo Finance through the [yfinance](https://ranaroussi.github.io/yfinance/) Python library.

The server uses [fastmcp](https://github.com/jlowin/fastmcp) and runs within a Docker container to ensure portability.

## Installation ##

- Using python & pip:
```
pip install .
```
- Alternative - using Docker:
```
docker build -t yfinance-mcp-server .
```


## Configuration ##

- If installed using python & pip, add this item in MCP settings:
```
"mcpServers": {
    "YahooFinanceServer": {
      "command": "python",
      "args": ["-m", "yfinance_mcp_server"]
    }
  }

```

- If installed using Docker, add this item in MCP settings:
```
"mcpServers": {
    "YahooFinanceServer": {
      "command": "docker",
      "args": ["run", "-i", "yfinance-mcp-server"]
    }
  }
```

## Example ##

In your LLM interface, e.g. Cline, you can ask something like:
```
What is MSFT's stock price on Jan 1, 2025?
```
