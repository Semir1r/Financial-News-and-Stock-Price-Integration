import talib as ta
import pandas as pd
import matplotlib.pyplot as plt

def apply_technical_indicators(df):
    # Calculate Simple Moving Average (SMA)
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    
    # Calculate Relative Strength Index (RSI)
    df['RSI_14'] = ta.RSI(df['Close'], timeperiod=14)
    
    # Calculate Moving Average Convergence Divergence (MACD)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df['Close'], 
                                                              fastperiod=12, 
                                                              slowperiod=26, 
                                                              signalperiod=9)
    

    
    return df

def calculate_financial_metrics(df):
    # Example: Calculate daily returns using PyNance
    df['daily_return'] = df['Close'].pct_change()
    

    return df

def load_stock_data(file_path):
    # Load the stock price data
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    
    # Ensure the data has the necessary columns
    required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    if not all(column in df.columns for column in required_columns):
        raise ValueError(f"Data must include the following columns: {required_columns}")
    
    
    return df

def visualize_stock_data(df):
    plt.figure(figsize=(14, 7))
    
    # Plot Closing Price
    plt.subplot(3, 1, 1)
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.plot(df.index, df['SMA_20'], label='20-Day SMA')
    plt.title('Stock Closing Price and SMA')
    plt.legend()
    
    # Plot RSI
    plt.subplot(3, 1, 2)
    plt.plot(df.index, df['RSI_14'], label='RSI (14)')
    plt.axhline(y=70, color='r', linestyle='--')
    plt.axhline(y=30, color='g', linestyle='--')
    plt.title('RSI (14)')
    plt.legend()
    
    # Plot MACD
    plt.subplot(3, 1, 3)
    plt.plot(df.index, df['MACD'], label='MACD')
    plt.plot(df.index, df['MACD_signal'], label='Signal Line')
    plt.bar(df.index, df['MACD_hist'], label='MACD Histogram')
    plt.title('MACD')
    plt.legend()
    
    plt.tight_layout()
    plt.show()