import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def test_stock_data(symbol='AAPL'):
    print(f"\nTesting data fetch for {symbol}...")
    try:
        stock = yf.Ticker(symbol)
        
        # Test 1: Direct Price Fetch
        print("\n1. Testing direct price fetch...")
        try:
            current = stock.fast_info['lastPrice']
            print(f"Current Price: {current}")
        except Exception as e:
            print(f"Error fetching price: {str(e)}")
        
        # Test 2: Historical Data
        print("\n2. Testing historical data...")
        try:
            end = datetime.now()
            start = end - timedelta(days=7)
            hist = stock.history(start=start, end=end)
            print(f"Data points: {len(hist)}")
            if not hist.empty:
                print(f"Latest close: {hist['Close'].iloc[-1]}")
                print(f"Available columns: {hist.columns.tolist()}")
        except Exception as e:
            print(f"Error fetching history: {str(e)}")
        
        # Test 3: Basic Info
        print("\n3. Testing basic info...")
        try:
            info = stock.fast_info
            for key, value in info.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error fetching info: {str(e)}")
        
        return True
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        return False

def main():
    print("Starting data fetch tests...")
    print("=" * 50)
    
    # Test multiple symbols
    symbols = ['AAPL', 'MSFT', 'GOOGL']
    results = {}
    
    for symbol in symbols:
        results[symbol] = test_stock_data(symbol)
    
    print("\nTest Results Summary:")
    print("=" * 50)
    for symbol, success in results.items():
        print(f"{symbol}: {'Success' if success else 'Failed'}")

if __name__ == "__main__":
    main()
