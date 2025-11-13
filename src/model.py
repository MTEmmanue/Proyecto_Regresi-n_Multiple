# src/model.py

import pandas as pd
import numpy as np
import joblib
# --- NUEVAS IMPORTACIONES ---
import matplotlib.pyplot as plt
import seaborn as sns
# --- FIN NUEVAS IMPORTACIONES ---

# Importa TODAS las rutas de config
from src.config import MODEL_PATH, RESULTS_PLOT_PATH 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


# --- NUEVA FUNCIÓN ---
def _save_results_plot(y_test, y_pred):
    """
    Función privada para guardar el gráfico de Reales vs. Predichos.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
    
    # Dibuja la línea diagonal perfecta (donde y_test == y_pred)
    # Encuentra los límites para la línea
    p1 = max(max(y_test), max(y_pred))
    p2 = min(min(y_test), min(y_pred))
    
    plt.plot([p1, p2], [p1, p2], 'r--') # 'r--' es una línea roja punteada
    
    plt.title('Valores Reales vs. Valores Predichos (Emisiones CO2)')
    plt.xlabel('Valores Reales (g/km)')
    plt.ylabel('Valores Predichos (g/km)')
    
    # Guarda el gráfico en la ruta de config
    plt.savefig(RESULTS_PLOT_PATH)
    print(f"Gráfico de resultados guardado en: {RESULTS_PLOT_PATH}")
# --- FIN NUEVA FUNCIÓN ---


def train_model(df):
    """
    Entrena el modelo de regresión lineal múltiple.
    """
    
    print("Iniciando entrenamiento del modelo...")
    
    # --- 1. Definir X e Y ---
    df_model = df.copy()
    y = df_model['co2_emissions(g/km)']
    X = df_model.drop('co2_emissions(g/km)', axis=1)
    X = X.select_dtypes(include=np.number)
    
    # --- 2. Dividir Datos (Train/Test) ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=42)
    
    # --- 3. Entrenar Modelo ---
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # --- 4. Evaluar Modelo ---
    y_pred = model.predict(X_test) # <--- ¡Aquí se generan las predicciones!
    
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse) 
    
    print("\n--- Evaluación del Modelo ---")
    print(f"R-squared (R2): {r2:.4f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print("------------------------------")

    # --- NUEVA LÍNEA ---
    # Llama a la función para guardar el gráfico
    _save_results_plot(y_test, y_pred)
    # --- FIN NUEVA LÍNEA ---

    # --- 5. Guardar Modelo ---
    print(f"Guardando modelo en: {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)
    
    return model