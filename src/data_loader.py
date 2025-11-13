# src/data_loader.py

import pandas as pd
from src.config import DATA_PATH  # <-- Importa la ruta desde tu config

def load_data():
    """
    Carga los datos desde la ruta especificada en config.py.
    """
    print(f"Cargando datos desde: {DATA_PATH}")
    return pd.read_csv(DATA_PATH)