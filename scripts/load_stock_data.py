import pandas as pd

def load_stock_data(filepath):
    """
    Load stock data from a CSV file.
    Ensure the file has the required columns: Open, High, Low, Close, Volume.
    """
    try:
        data = pd.read_csv(filepath)
        
        # Validate required columns
        required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Missing required columns in the file: {filepath}")
        
        # Parse the date column if available
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            data.set_index('Date', inplace=True)
        
        return data
    
    except Exception as e:
        raise RuntimeError(f"Error loading stock data from {filepath}: {e}")
