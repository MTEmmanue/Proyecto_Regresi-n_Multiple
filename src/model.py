# src/model.py

import pandas as pd
import numpy as np
import joblib
from src.config import MODEL_PATH
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def train_model(df):
    """
    Entrena el modelo de regresión lineal múltiple:
    - Define X (predictores) e Y (objetivo).
    - Divide los datos en entrenamiento y prueba.
    - Entrena el modelo.
    - Evalúa el modelo (R2 y MSE).
    - Guarda el modelo entrenado en disco.
    """
    
    print("Iniciando entrenamiento del modelo...")
    
    # --- 1. Definir X e Y ---
    # 'co2_emissions(g/km)' es nuestro objetivo
    # Usamos .copy() para evitar advertencias de Pandas
    df_model = df.copy()
    
    # Definimos el objetivo (Y)
    y = df_model['co2_emissions(g/km)']
    
    # Definimos los predictores (X)
    # Quitamos la columna objetivo
    X = df_model.drop('co2_emissions(g/km)', axis=1)
    
    # Asegurarnos de usar SOLO columnas numéricas para el modelo
    # Esto es clave, ya que descarta cualquier columna de texto que haya quedado
    X = X.select_dtypes(include=np.number)
    
    # --- 2. Dividir Datos (Train/Test) ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=42)
    
    # --- 3. Entrenar Modelo ---
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # --- 4. Evaluar Modelo ---
    y_pred = model.predict(X_test)
    
    # Calculamos las métricas
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse) # Root Mean Squared Error es más interpretable
    
    print("\n--- Evaluación del Modelo ---")
    print(f"R-squared (R2): {r2:.4f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print("------------------------------")
    
    # --- 5. Guardar Modelo ---
    # (Este paso cumple con tu Issue de GitHub)
    print(f"Guardando modelo en: {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)
    
    return model