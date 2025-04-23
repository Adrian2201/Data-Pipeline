
# etl.py

import pandas as pd
import os

def extract(path):
    return pd.read_csv(path)

def transform(df):
    # Calcula o total de vendas
    df["Total"] = df["Quantidade"] * df["Preço Unitário"]
    return df

def load(df, path):
    # Garante que a pasta exista
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    raw_path       = "data_lake/raw/vendas.csv"
    processed_path = "data_lake/processed/vendas_transformadas.csv"

    # ETL
    df_raw         = extract(raw_path)
    df_transformed = transform(df_raw)
    load(df_transformed, processed_path)

    print(f"ETL concluído! Arquivo gerado em: {processed_path}")
