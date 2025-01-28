import yfinance as yf
import pandas as pd
import requests

def test_network():
    print("\nTesting network connectivity...")
    try:
        response = requests.get("https://finance.yahoo.com")
        print(f"Yahoo Finance website status code: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Network error: {str(e)}")
        return False

def test_yfinance():
    print("\nTesting YFinance functionality...")
    
    # Test with a single well-known ticker
    ticker = "AAPL"
    try:
        print(f"\nTesting data fetch for {ticker}")
        stock = yf.Ticker(ticker)
        
        # Try to get info first
        print("Fetching stock info...")
        info = stock.info
        print(f"Company Name: {info.get('longName', 'N/A')}")
        
        # Try different period lengths
        for period in ["1d", "5d", "1mo"]:
            print(f"\nTrying period: {period}")
            hist = stock.history(period=period)
            
            if hist.empty:
                print(f"No data received for period {period}")
            else:
                print(f"Success! Received data for period {period}")
                print(f"Data shape: {hist.shape}")
                print("Latest data point:")
                print(hist.tail(1))
                
    except Exception as e:
        print(f"Error during test: {str(e)}")

if __name__ == "__main__":
    if test_network():
        print("Network connection successful, testing YFinance...")
        test_yfinance()
    else:
        print("Network connection failed. Please check your internet connection and proxy settings.")
