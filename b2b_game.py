import streamlit as st
import pandas as pd
import random
import time

# ---- Configuración página ----
st.set_page_config(
    page_title="🎯 Mini B2B Sales Challenge - Modo Killer",
    layout="wide",
    page_icon="🎯"
)

# ---- Estilo de fondo con imagen premium ----
st.markdown("""
    <style>
    body {
        background-image: url('https://www.example.com/background-premium.jpg'); /* URL de la imagen elegante */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .title {
        color: #4B0082;
        font-size: 36px;
    }
    .subtitle {
        font-size: 18px;
        font-weight: bold;
    }
    .button {
        background-color: #FF5733;
        font-size: 20px;
        color: white;
        padding: 15px 30px;
        border-radius: 50px;
        cursor: pointer;
        border: none;
    }
    .button:hover {
        background-color: #C13D26;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Branding Premium ----
st.markdown("""
<div style='display:flex; justify-content:space-between; align-items:center'>
<h1 class="title">🎯 Mini B2B Sales Challenge - Modo Killer</h1>
<span class="subtitle">@Monik</span>
</div>
<p style='font-size:18px;'>Toma decisiones estratégicas y maximiza tu impacto en ventas B2B.  
Elige tu estrategia y observa cómo impactan tus resultados con cada cliente de tu cartera. ¡Diversión garantizada! 💼🎡</p>
<hr>
""", unsafe_allow_html=True)

# ---- Instrucciones Iniciales ----
st.markdown("""
### **¿Cómo jugar?**
1. **Elige un cliente** de tu cartera.
2. **Selecciona una estrategia** para ese cliente.
3. **Mira los resultados dinámicos**: ¡Cada decisión tiene un impacto!
4. **Cuando termines**, ¡Gira la ruleta de premios para ver qué ganaste! 🎉
""")

# ---- Clientes ----
clients = [
    {"nombre": "Cuenta A - Energía", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología", "potencial": 100000, "relacion": "baja"},
    {"nombre": "Cuenta D - Salud", "potencial": 200000, "relacion": "media"},
    {"nombre": "Cuenta E - Retail", "potencial": 400000, "relacion": "buena"}
]

# ---- Inicializar sesión ----
if "historial" not in st.session_state:
    st.session_state.historial = pd.DataFrame({
        "Cuenta": [c["nombre"] for c in clients],
        "Estrategia": ["" for _ in clients],
        "Impacto": [0 for _ in clients],
        "Semaforo": ["" for _ in clients]
    })

if "impacto_total" not in st.session_state:
    st.session_state.impacto_total = 0

# ---- Función semáforo ----
def semaforo(factor):
    if factor >= 0.9:
        return "🟢 Excelente"
    elif factor >= 0.6:
        return "🟡 Bien"
    else:
        return "🔴 Riesgo"

# ---- Estrategias disponibles ----
strategies = {
    "🎯 Priorizar demo personalizada": 1.0,
    "💼 Negociar descuento estratégico": 0.7,
    "⚡ Ignorar objeciones y cerrar rápido": 0.3
}

# ---- Mostrar clientes en cards con botones ----
st.markdown("### Tu cartera de clientes")
cols = st.columns(len(clients))  # Crea una columna por cada cliente

# Iteramos sobre los clientes y mostramos botones para elegir estrategias
for i, client in enumerate(clients):
    with cols[i]:
        st.markdown(f"**{client['nombre']}**")
        st.markdown(f"Relación: {client['relacion'].capitalize()}")
        st.markdown(f"Potencial: ${client['potencial']:,}")

        if st.session_state.historial.loc[i, "Estrategia"] == "":
            # Mostrar botones de estrategias disponibles
            for label, factor in strategies.items():
                if st.button(label, key=f"{i}-{label}"):
                    impacto = client["potencial"] * factor
                    st.session_state.historial.loc[i, "Estrategia"] = label
                    st.session_state.historial.loc[i, "Impacto"] = impacto
                    st.session_state.historial.loc[i, "Semaforo"] = semaforo(factor)
                    st.session_state.i_
