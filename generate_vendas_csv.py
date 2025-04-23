# generate_vendas_csv.py

import pandas as pd
import numpy as np
from pathlib import Path

# Definir pasta raw
raw_dir = Path("data_lake/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

# Gerar dados de exemplo
np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=100, freq="D")
produtos = [f"Produto {chr(65 + i % 5)}" for i in range(100)]
categorias = [f"Categoria {1 + (i % 3)}" for i in range(100)]
quantidades = np.random.randint(1, 20, size=100)
precos = np.round(np.random.uniform(10, 100, size=100), 2)
regioes = np.random.choice(["Região 1", "Região 2", "Região 3"], size=100)
vendedores = np.random.choice([f"Vendedor {i}" for i in range(1, 6)], size=100)

# Montar DataFrame
df = pd.DataFrame({
    "Data": dates,
    "Produto": produtos,
    "Categoria": categorias,
    "Quantidade": quantidades,
    "Preço Unitário": precos,
    "Região": regioes,
    "Vendedor": vendedores
})

# Salvar CSV
out_path = raw_dir / "vendas.csv"
df.to_csv(out_path, index=False)
print(f"Arquivo gerado: {out_path} ({len(df)} linhas)")

