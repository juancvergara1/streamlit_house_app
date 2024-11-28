import streamlit as st
import pandas as pd
from joblib import load

# Cargar el modelo desde el archivo .pkl
model_path = "house_price_model.pkl"  # Ruta al modelo guardado
loaded_model = load(model_path)

# Título de la aplicación
st.title("Predicción del Precio de la Vivienda")

# Instrucciones
st.write("Introduce los detalles de la vivienda para predecir su precio.")

# Entradas del usuario
st.header("Ingrese los detalles de la vivienda:")
square_footage = st.number_input("Metros cuadrados", min_value=10, max_value=10000, value=100)
num_bedrooms = st.number_input("Número de habitaciones", min_value=1, max_value=20, value=3)
num_bathrooms = st.number_input("Número de baños", min_value=1, max_value=20, value=2)
year_built = st.number_input("Año de construcción", min_value=1800, max_value=2024, value=2000)
lot_size = st.number_input("Tamaño del lote (m²)", min_value=10.0, max_value=10000.0, value=500.0)
garage_size = st.number_input("Tamaño del garaje (autos)", min_value=0, max_value=10, value=2)
neighborhood_quality = st.number_input("Calidad del vecindario (1-10)", min_value=1, max_value=10, value=5)

# Crear un DataFrame con las entradas
input_data = pd.DataFrame({
    "Square_Footage": [square_footage],
    "Num_Bedrooms": [num_bedrooms],
    "Num_Bathrooms": [num_bathrooms],
    "Year_Built": [year_built],
    "Lot_Size": [lot_size],
    "Garage_Size": [garage_size],
    "Neighborhood_Quality": [neighborhood_quality],
})

# Predicción
if st.button("Predecir Precio"):
    try:
        prediction = loaded_model.predict(input_data)
        st.success(f"El precio estimado de la vivienda es: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Ocurrió un error al realizar la predicción: {e}")
