import pandas as pd

def load_and_clean_data(path):
    # Load dataset
    df = pd.read_csv(path)
    
    # Fill missing values with column mean
    df.fillna(df.mean(), inplace=True)
    
    return df
