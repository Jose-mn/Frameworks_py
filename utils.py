# utils.py
import pandas as pd

def load_and_clean(path='metadata.csv'):
    df = pd.read_csv(path, low_memory=False)
    df = df.dropna(subset=['title','publish_time']).copy()
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df = df.dropna(subset=['publish_time'])
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna('')
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))
    return df
