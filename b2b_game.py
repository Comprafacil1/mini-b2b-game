# b2b_game.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time

# ---- Configuración de la página ----
st.set_page_config(page_title="🎯 Mini-Juego B2B Sales", layout="wide")

# ---- Título ----
st.markdown("## 🎯 Mini-Juego B2B Sales")
st.markdown("Demuestra tu habilidad en **ventas complejas** y gestión de cuentas")

# ---- Datos de ejemplo ----
accounts = [
    {"nombre": "Cuenta A - Energía", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología", "potencial": 100000, "relacion": "baja"}
]

# ---- Prioridades del jugador ----
st.markdown("### Instrucciones")
st.markdown("Tienes 3 cuentas estratégicas. Prioriza según **ingresos potenciales** y **fidelización C-Level**.")

priorities = {}
for acc in accounts:
    priorities[acc["nombre"]] = st.radio(
        f"¿Qué prioridad le das a {acc['nombre']}?",
        ("Alta", "Media", "Baja")
    )

# ---- Calculamos impacto ----
impact_total = 0
for acc in accounts:
    factor = {"Alta": 1, "Media": 0.6, "Baja": 0.3}[priorities[acc["nombre"]]]
    impact_total += acc["potencial"] * factor

st.markdown(f"### 💰 Potencial total impactado: ${impact_total:,.0f}")

# ---- Tabla resumen ----
df = pd.DataFrame({
    "Cuenta": [acc["nombre"] for acc in accounts],
    "Potencial ($)": [acc["potencial"] for acc in accounts],
    "Relación C-Level": [acc["relacion"] for acc in accounts],
    "Prioridad tuya": [priorities[acc["nombre"]] for acc in accounts]
})
st.markdown("### Resumen de decisiones")
st.table(df)

# ---- Gráfico con animación ----
fig, ax = plt.subplots(figsize=(8,5))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # azul, naranja, verde
bars = ax.bar(df["Cuenta"], [0]*len(df), color=colors)

ax.set_ylabel("Potencial ($)")
ax.set_title("Impacto por Cuenta")

# Animación de carga de barras
for i, bar in enumerate(bars):
    for height in range(0, df["Potencial ($)"][i]+1, int(df["Potencial ($)"][i]/50)):
        bar.set_height(height)
        plt.pause(0.01)
        st.pyplot(fig, clear_figure=True)

# Valores sobre las barras
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"${int(bar.get_height()):,}",
        ha='center', va='bottom', fontsize=10, color='black'
    )

st.pyplot(fig)

# ---- Mensaje final ----
st.markdown(
    """
    🚀 **Comparte tu resultado en LinkedIn**  
    Impresiona a tu red profesional compartiendo tu puntaje y decisiones B2B.
    """
)

# ---- Branding discreto ----
st.markdown(
    """
    <div style="position: fixed; bottom: 10px; right: 10px; font-size:12px; color: gray;">
        @Monik
    </div>
    """,
    unsafe_allow_html=True
)
