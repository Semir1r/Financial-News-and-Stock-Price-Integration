import pandas as pd

def normalize_dates(news_df, stock_df, date_format='%Y-%m-%d'):
    try:
        news_df['date'] = pd.to_datetime(news_df['date'], utc=True, errors='coerce')
        stock_df['Date'] = pd.to_datetime(stock_df['Date'], utc=True, errors='coerce')
        news_df['date'] = news_df['date'].dt.strftime(date_format)
        stock_df['Date'] = stock_df['Date'].dt.strftime(date_format)
    except Exception as e:
        print(f"Error processing dates: {e}")
        return None

    try:
        merged_df = pd.merge(news_df, stock_df, left_on=['date', 'stock'], right_on=['Date', 'stock'], how='inner')
        return merged_df
    except Exception as e:
        print(f"Error merging data: {e}")
        return None