# Creando git# main.py

# Importa las funciones de tus módulos en 'src'
from src.data_loader import load_data
from src.data_clean import clean_data
from src.data_processing import preprocess_features
from src.model import train_model


# Importa esta librería para limpiar la terminal (opcional pero útil)
import os

def main():
    """
    Orquesta todo el pipeline de Machine Learning.
    """
    os.system('cls' if os.name == 'nt' else 'clear') # Limpia la terminal
    print("==============================================")
    print("== 🚀 INICIANDO PIPELINE DE EMISIONES CO2 ==")
    print("==============================================")
    
    # 1. Cargar datos
    print("\n[PASO 1/4] Cargando datos...")
    data = load_data()
    
    # 2. Limpiar datos
    print("[PASO 2/4] Limpiando datos...")
    data_clean = clean_data(data)
    
    # 3. Preprocesar features
    print("[PASO 3/4] Preprocesando features...")
    data_processed = preprocess_features(data_clean)
    
    # 4. Entrenar modelo
    print("[PASO 4/4] Entrenando y evaluando modelo...")
    model = train_model(data_processed)
    
    print("\n==============================================")
    print("== ✅ PIPELINE FINALIZADO EXITOSAMENTE ==")
    print("==============================================")

# Esta línea estándar de Python asegura que main() solo se ejecute
# cuando corres el script directamente.
if __name__ == "__main__":
    main()