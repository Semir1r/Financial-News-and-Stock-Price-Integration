import os
import pandas as pd

def load_and_concatenate_stock_data(file_paths):
    data_frames = []
    for file_path in file_paths:
        stock_symbol = os.path.basename(file_path).split('_')[0]
        df = pd.read_csv(file_path)
        df['stock'] = stock_symbol  # Adding 'stock' column
        data_frames.append(df)
    return pd.concat(data_frames, ignore_index=True)