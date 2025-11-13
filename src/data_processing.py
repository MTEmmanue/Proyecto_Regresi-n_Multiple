# src/data_processing.py

import pandas as pd

def preprocess_features(df):
    """
    Pre-procesa las features:
    - Aplica One-Hot Encoding a la columna categórica 'fuel_type'.
    """
    
    # Hacemos una copia para evitar advertencias
    df_processed = df.copy()
    
    # Aplicamos One-Hot Encoding.
    # Esto convertirá 'fuel_type' en múltiples columnas (ej. 'fuel_type_D', 'fuel_type_E')
    # con valores 0 o 1.
    # 'drop_first=True' es una buena práctica para evitar multicolinealidad.
    df_processed = pd.get_dummies(df_processed, 
                                  columns=['fuel_type'], 
                                  drop_first=True, 
                                  dtype=int) # dtype=int para que sean 0s y 1s
    
    print("Preprocesamiento completado (One-Hot Encoding aplicado).")
    return df_processed