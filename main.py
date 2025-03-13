
import pandas as pd
import io

def load_csv(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        return str(e)
