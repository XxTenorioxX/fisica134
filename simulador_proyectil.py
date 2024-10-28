# simulador_proyectil.py
import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la página
st.title("Simulador de la Trayectoria de un Proyectil")
st.write("Aplicación de física para simular la trayectoria de un proyectil.")

# Función para calcular la distancia máxima de un proyectil
def calcular_distancia_maxima(angulo, velocidad):
    angulo_rad = math.radians(angulo)
    distancia = (velocidad ** 2) * math.sin(2 * angulo_rad) / 9.81
    return distancia

# Inputs del usuario para el ángulo y la velocidad
angulo = st.number_input("Ingresa el ángulo de lanzamiento (grados):", min_value=0, max_value=90, value=45)
velocidad = st.number_input("Ingresa la velocidad inicial (m/s):", min_value=1, value=20)

# Botón para calcular la distancia máxima
if st.button("Calcular distancia máxima"):
    distancia_maxima = calcular_distancia_maxima(angulo, velocidad)
    st.write(f"La distancia máxima es: {distancia_maxima:.2f} metros")

# Botón para verificar la respuesta
if st.button("Mostrar trayectoria"):
    # Calcular la trayectoria
    angulo_rad = math.radians(angulo)
    t_total = 2 * velocidad * math.sin(angulo_rad) / 9.81
    t = np.linspace(0, t_total, num=500)
    x = velocidad * np.cos(angulo_rad) * t
    y = velocidad * np.sin(angulo_rad) * t - 0.5 * 9.81 * t ** 2

    # Graficar la trayectoria
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title("Trayectoria del proyectil")
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.ylim(bottom=0)
    st.pyplot(plt)
