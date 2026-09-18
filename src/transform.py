import pandas as pd


def clean_employees(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["salary"] = pd.to_numeric(df["salary"])

    return df


def clean_orders(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["quantity"] = pd.to_numeric(df["quantity"])
    df["price"] = pd.to_numeric(df["price"])

    df["total_amount"] = df["quantity"] * df["price"]

    return df
