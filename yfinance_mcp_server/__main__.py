import yfinance as yf
from fastmcp import FastMCP
import argparse
import asyncio

mcp = FastMCP(name="yfiannce MCP Server",
            instructions="Provides a set of tools to interact with Yahoo Finance API through yfinance to retrieve stock market data.",
            version="0.1.0")

def get_ticker(ticker: str):
    """
    Get a yfinance Ticker object for a given symbol.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
    
    Returns:
        yfinance.Ticker: A yfinance Ticker instance.
    """
    return yf.Ticker(ticker)


@mcp.tool
def get_company_info(ticker: str) -> dict:
    """
    Retrieve a summary of company information for a given ticker.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary of key company information including sector, industry, full name, etc.
    """
    return get_ticker(ticker).get_info()


@mcp.tool
def get_history(ticker: str, period: str = "1mo", interval: str = "1d") -> dict:
    """
    Get historical stock price data.

    Args:
        ticker (str): Stock ticker symbol.
        period (str, optional): Time period (e.g., '1d', '5d', '1mo', '1y', etc.).
        interval (str, optional): Data interval (e.g., '1m', '5m', '1d', '1wk').

    Returns:
        dict: Historical OHLCV data as a list of dictionaries.
    """
    df = get_ticker(ticker).history(period=period, interval=interval)
    return df.reset_index().to_dict(orient="records")


@mcp.tool
def get_financials(ticker: str) -> dict:
    """
    Get the annual income statement for a company.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: A dictionary representation of the company's income statement.
    """
    return get_ticker(ticker).financials.to_dict()


@mcp.tool
def get_balance_sheet(ticker: str) -> dict:
    """
    Retrieve the annual balance sheet of a company.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: Balance sheet data keyed by account and year.
    """
    return get_ticker(ticker).balance_sheet.to_dict()


@mcp.tool
def get_cashflow(ticker: str) -> dict:
    """
    Retrieve the annual cash flow statement of a company.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: Cash flow data including operating, investing, and financing activities.
    """
    return get_ticker(ticker).cashflow.to_dict()


@mcp.tool
def get_dividends(ticker: str) -> dict:
    """
    Get historical dividend payout data for a given stock.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: List of dividend payment dates and amounts.
    """
    df = get_ticker(ticker).dividends
    return df.reset_index().to_dict(orient="records")


@mcp.tool
def get_earnings(ticker: str) -> dict:
    """
    Retrieve the annual earnings report for a company.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: Earnings data including revenue and earnings.
    """
    return get_ticker(ticker).earnings.to_dict()


@mcp.tool
def get_calendar(ticker: str) -> dict:
    """
    Get upcoming calendar events like earnings report dates.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: Calendar events (usually includes next earnings date).
    """
    return get_ticker(ticker).calendar.to_dict()


@mcp.tool
def get_options(ticker: str) -> list:
    """
    Retrieve available options expiration dates for a stock.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        list: A list of expiration date strings (e.g., ['2025-07-05', ...]).
    """
    return get_ticker(ticker).options


@mcp.tool
def get_option_chain(ticker: str, expiration: str) -> dict:
    """
    Retrieve the option chain (calls and puts) for a specific expiration date.

    Args:
        ticker (str): Stock ticker symbol.
        expiration (str): Expiration date (e.g., '2025-07-05').

    Returns:
        dict: A dictionary with 'calls' and 'puts' containing option contract details.
    """
    chain = get_ticker(ticker).option_chain(expiration)
    return {
        "calls": chain.calls.to_dict(orient="records"),
        "puts": chain.puts.to_dict(orient="records")
    }




parser = argparse.ArgumentParser(
    description="Provides a set of tools to interact with Yahoo Finance API through yfinance to retrieve stock market data."
)

args = parser.parse_args()
mcp.run()  # Default: uses STDIO transport
