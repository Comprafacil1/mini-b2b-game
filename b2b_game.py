import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# ---- Configuración página ----
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
<p style='font-size:18px;'>Toma decisiones estratégicas y maximiza tu impacto en ventas B2B.  
Todos los clientes de tu cartera visibles, elige tu estrategia y observa resultados dinámicos.</p>
<hr>
""", unsafe_allow_html=True)

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

# ---- Estrategias ----
strategies = {
    "🎯 Priorizar demo personalizada": 1.0,
    "💼 Negociar descuento estratégico": 0.7,
    "⚡ Ignorar objeciones y cerrar rápido": 0.3
}

# ---- Mostrar clientes en cards con botones ----
st.markdown("### Tu cartera de clientes")
cols = st.columns(len(clients))

for i, client in enumerate(clients):
    with cols[i]:
        st.markdown(f"**{client['nombre']}**")
        st.markdown(f"Relación: {client['relacion'].capitalize()}")
        st.markdown(f"Potencial: ${client['potencial']:,}")

        if st.session_state.historial.loc[i, "Estrategia"] == "":
            for label, factor in strategies.items():
                if st.button(label, key=f"{i}-{label}"):
                    impacto = client["potencial"] * factor
                    st.session_state.historial.loc[i, "Estrategia"] = label
                    st.session_state.historial.loc[i, "Impacto"] = impacto
                    st.session_state.historial.loc[i, "Semaforo"] = semaforo(factor)
                    st.session_state.impacto_total += impacto
                    st.experimental_rerun()
        else:
            # Aquí estaba el error de indentación
            st.markdown(f"**Estrategia elegida:** {st.session_state.historial.loc[i, 'Estrategia']}")
            st.markdown(f"**Impacto:** ${st.session_state.historial.loc[i, 'Impacto']:,}")
            st.markdown(f"{st.session_state.historial.loc[i, 'Semaforo']}")

# ---- Gráfico de barras dinámico ----
st.markdown("---")
st.markdown("### Impacto por cliente")
impact_data = pd.DataFrame({
    "Cliente": st.session_state.historial["Cuenta"],
    "Impacto": st.session_state.historial["Impacto"]
}).set_index("Cliente")
st.bar_chart(impact_data)

# ---- Barra de impacto total ----
st.markdown("### Impacto total acumulado")
st.metric(label="Impacto total", value=f"${int(st.session_state.impacto_total):,}")

# ---- Juego completado ----
if all(st.session_state.historial["Estrategia"] != ""):
    st.markdown("---")
    st.markdown("### 🎡 Ruleta de premios")
    if "ruleta_girada" not in st.session_state:
        st.session_state.ruleta_girada = False

    if not st.session_state.ruleta_girada and st.button("Girar ruleta"):
        premios = [
            "🍖 Te ganaste un asado virtual!",
            "🔄 Vuelve pronto",

