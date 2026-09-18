import pandas as pd


def extract_employees(file_path):
    return pd.read_csv(file_path)


def extract_orders(file_path):
    return pd.read_csv(file_path)
