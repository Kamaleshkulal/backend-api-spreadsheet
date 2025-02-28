import pandas as pd

def trim(text):
    return text.strip()

def upper(text):
    return text.upper()

def lower(text):
    return text.lower()

def remove_duplicates(df):
    return df.drop_duplicates()

def find_and_replace(df, find_text, replace_text):
    return df.replace(find_text, replace_text)