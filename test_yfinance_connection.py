import yfinance as yf
import pandas as pd
from datetime import datetime
import requests

def test_yahoo_connection():
    """Test direct connection to Yahoo Finance"""
    try:
        response = requests.get("https://finance.yahoo.com", timeout=5)
        print(f"Yahoo Finance website connection: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error connecting to Yahoo Finance: {str(e)}")
        return False

def test_stock_data(symbol="AAPL"):
    """Test fetching stock data"""
    try:
        print(f"\nTesting data fetch for {symbol}")
        stock = yf.Ticker(symbol)
        
        # Test basic info
        print("\nFetching basic info...")
        info = stock.info
        if info:
            print(f"Company Name: {info.get('longName', 'N/A')}")
            print(f"Current Price: {info.get('currentPrice', 'N/A')}")
            print(f"Market Cap: {info.get('marketCap', 'N/A')}")
        else:
            print("Could not fetch basic info")
        
        # Test historical data
        print("\nFetching historical data...")
        hist = stock.history(period="1d")
        if not hist.empty:
            print("Historical data:")
            print(hist)
        else:
            print("No historical data received")
        
        # Test financials
        print("\nFetching financial data...")
        financials = stock.financials
        if not financials.empty:
            print("\nFinancial data available")
        else:
            print("No financial data available")
            
    except Exception as e:
        print(f"Error in data fetch: {str(e)}")

if __name__ == "__main__":
    print("Testing YFinance Connection...")
    print(f"Current time: {datetime.now()}")
    print(f"YFinance version: {yf.__version__}")
    
    if test_yahoo_connection():
        print("\nConnection successful, testing data fetch...")
        test_stock_data()
    else:
        print("\nCannot connect to Yahoo Finance. Please check your internet connection or proxy settings.")
