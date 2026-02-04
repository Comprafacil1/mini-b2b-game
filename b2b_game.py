# b2b_game_visual.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# ---- Configuración de la página ----
st.set_page_config(
    page_title="🎯 Mini B2B Sales Challenge - Modo Killer",
    layout="wide",
    page_icon="🎯"
)

# ---- Branding premium ----
st.markdown("""
<div style='display:flex; justify-content:space-between; align-items:center'>
<h1 style='color:#4B0082;'>🎯 Mini B2B Sales Challenge - Modo Killer</h1>
<span style='font-size:18px; font-weight:bold'>@Monik</span>
</div>
<p style='font-size:18px;'>Demuestra tu capacidad de tomar decisiones estratégicas y maximizar impacto en ventas B2B.</p>
""", unsafe_allow_html=True)
st.markdown("---")

# ---- Clientes / Desafíos ----
clients = [
    {"nombre": "Cuenta A - Energía", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología", "potencial": 100000, "relacion": "baja"}
]

# ---- Inicializar estado ----
if "ronda" not in st.session_state:
    st.session_state.ronda = 0
if "impacto_total" not in st.session_state:
    st.session_state.impacto_total = 0
if "historial" not in st.session_state:
    st.session_state.historial = []

# ---- Función para mostrar semáforo ----
def semaforo(factor):
    if factor >= 0.9:
        return "🟢 Excelente"
    elif factor >= 0.6:
        return "🟡 Bien"
    else:
        return "🔴 Riesgo"

# ---- Mostrar cliente actual ----
if st.session_state.ronda < len(clients):
    client = clients[st.]()

