
# MCP Server for Interacting with Yahoo Finance #

---

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open standard developed by Anthropic to enable seamless integration between Large Language Models (LLMs) and external tools, services, and data sources.

This project provides a simple implementation that allows LLM to interact with Yahoo Finance through the [yfinance](https://ranaroussi.github.io/yfinance/) Python library.

The server uses [fastmcp](https://github.com/jlowin/fastmcp) and runs within a Docker container to ensure portability.

## Install and Run ##

- Install package:
```
pip install .
```
- Add this item in MCP settings:
```
"mcpServers": {
    "YahooFinanceServer": {
      "command": "python",
      "args": ["-m", "yfinance_mcp_server"]
    }
  }

```

## Alternative - Build and Run using Docker ##

The preferred way is to use Docker so you don't run into dependency issues.
- To build the container:
```
docker build -t yfinance-mcp-server .
```
- Add this item in MCP settings:
```
"mcpServers": {
    "YahooFinanceServer": {
      "command": "docker",
      "args": ["run", "-i", "yfinance-mcp-server"]
    }
  }
```


In your LLM interface, you can ask something like:
```
What is MSFT's stock price on Jan 1, 2025?
```
