# b2b_game.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# --- Configuración ---
st.set_page_config(page_title="Mini-Juego B2B Sales", layout="wide")

st.markdown("<h1 style='text-align: center;'>🎯 Mini-Juego B2B Sales</h1>", unsafe_allow_html=True)
st.write("Demuestra tu habilidad en ventas complejas y gestión de cuentas")

# --- Datos de cuentas ---
accounts = [
    {"nombre": "Cuenta A - Energía ⚡", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería ⛏️", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología 💻", "potencial": 100000, "relacion": "baja"}
]

# --- Instrucciones ---
st.subheader("Instrucciones:")
st.write("""
- Tienes 3 cuentas estratégicas.  
- Prioriza las cuentas según ingresos potenciales y fidelización C-Level.  
- Observa el impacto de tus decisiones en el negocio.
""")

# --- Selección de prioridades ---
st.subheader("Prioriza tus cuentas:")
priorities = []
for info in accounts:
    p = st.radio(
        f"¿Qué prioridad le das a {info['nombre']}?",
        ["Alta 🔴", "Media 🟡", "Baja 🟢"],
        key=info['nombre']
    )
    priorities.append(p)

# --- Calcular puntaje ---
score = 0
for i, info in enumerate(accounts):
    if priorities[i].startswith("Alta"):
        if info["relacion"] == "buena":
            score += info["potencial"] * 0.5
        elif info["relacion"] == "media":
            score += info["potencial"] * 0.3
        else:
            score += info["potencial"] * 0.1
    elif priorities[i].startswith("Media"):
        if info["relacion"] == "buena":
            score += info["potencial"] * 0.3
        elif info["relacion"] == "media":
            score += info["potencial"] * 0.2
        else:
            score += info["potencial"] * 0.05
    else:
        score += 0

# --- Mostrar puntaje ---
st.subheader("Impacto de tus decisiones")
st.markdown(f"💰 **Potencial total impactado:** ${int(score):,}")

# --- Gráfico de barras estilo premium ---
fig, ax = plt.subplots(figsize=(8,4))
names = [info["nombre"] for info in accounts]
potenciales = [info["potencial"] for info in accounts]

# Colores degradados según prioridad
color_map = {"Alta 🔴": "#FF4C4C", "Media 🟡": "#FFC107", "Baja 🟢": "#4CAF50"}
colors = [color_map[p] for p in priorities]

bars = ax.bar(names, potenciales, color=colors, edgecolor='black')
ax.set_ylabel("Potencial ($)")
ax.set_title("Impacto de tu priorización")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Mostrar valores encima de las barras
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() +_
