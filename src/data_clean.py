# src/data_cleaning.py

def clean_data(df):
    """
    Limpia los datos:
    - Renombra columnas a un formato 'pythonico' (minúsculas y guiones bajos).
    - (Este es el lugar donde manejarías valores nulos si los tuvieras).
    """
    
    # Hacemos una copia para evitar advertencias de "SettingWithCopyWarning"
    df_clean = df.copy()
    
    # Renombrar columnas: 'Fuel Type' -> 'fuel_type'
    df_clean.columns = df_clean.columns.str.replace(' ', '_').str.lower()
    
    # Para este dataset, los valores nulos no son un problema.
    # Si lo fueran, aquí aplicarías:
    # df_clean = df_clean.dropna()
    
    print("Datos limpiados (columnas renombradas).")
    return df_clean