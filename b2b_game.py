# b2b_game_premium.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time

# ---- Configuración de la página ----
st.set_page_config(page_title="🎯 Mini B2B Sales Challenge", layout="wide")

# ---- Branding premium ----
st.markdown("<h1 style='text-align:center; color:#4B0082;'>🎯 Mini B2B Sales Challenge</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Demuestra tu capacidad para priorizar cuentas estratégicas y generar impacto real en ventas B2B.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---- Datos de ejemplo ----
accounts = [
    {"nombre": "Cuenta A - Energía", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología", "potencial": 100000, "relacion": "baja"}
]

# ---- Prioridades del jugador ----
st.markdown("### Instrucciones")
st.markdown("Asigna prioridades a cada cuenta según **potencial de ingresos** y **relación con C-Level**:")

priorities = {}
feedback = {}
for acc in accounts:
    priorities[acc["nombre"]] = st.radio(
        f"¿Qué prioridad le das a {acc['nombre']}?",
        ("Alta", "Media", "Baja"),
        key=acc["nombre"]
    )
    # Feedback educativo
    if priorities[acc["nombre"]] == "Alta":
        feedback[acc["nombre"]] = "Buena decisión, maximizas impacto en cuentas clave."
    elif priorities[acc["nombre"]] == "Media":
        feedback[acc["nombre"]] = "Decisión equilibrada, podrías mejorar priorizando cuentas de mayor potencial."
    else:
        feedback[acc["nombre"]] = "Prioridad baja asignada, podrías perder oportunidades importantes."

# ---- Botón de cálculo ----
if st.button("Calcular Impacto"):
    # Calculamos impacto
    impact_total = 0_
