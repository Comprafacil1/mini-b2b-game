# b2b_game_premium.py
import streamlit as st
import pandas as pd
import random
import time
import matplotlib.pyplot as plt

# ---- Configuración de página ----
st.set_page_config(
    page_title="🎯 Mini B2B Sales Challenge - Modo Killer Fun",
    layout="wide",
    page_icon="🎯"
)

# ---- Branding premium con nombre ----
st.markdown("""
<div style='display:flex; justify-content:space-between; align-items:center'>
<h1 style='color:#4B0082;'>🎯 Mini B2B Sales Challenge - Modo Killer</h1>
<span style='font-size:18px; font-weight:bold'>@Monik</span>
</div>
<p style='font-size:18px;'>Toma decisiones estratégicas y diviértete como si fueras niño jugando a ventas B2B.</p>
""", unsafe_allow_html=True)
st.markdown("---")

# ---- Clientes ----
clients = [
    {"nombre": "Cuenta A - Energía", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología", "potencial": 100000, "relacion": "baja"},
    {"nombre": "Cuenta D - Salud", "potencial": 200000, "relacion": "media"},
    {"nombre": "Cuenta E - Retail", "potencial": 400000, "relacion": "buena"}
]

# ---- Inicializar sesión ----
if "ronda" not in st.session_state:
    st.session_state.ronda = 0
if "impacto_total" not in st.session_state:
    st.session_state.impacto_total = 0
if "historial" not in st.session_state:
    st.session_state.historial = []

# ---- Función semáforo ----
def semaforo(factor):
    if factor >= 0.9:
        return "🟢 Excelente"
    elif factor >= 0.6:
        return "🟡 Bien"
    else:
        return "🔴 Riesgo"

# ---- Función ruleta ----
def ruleta_premio():
    premios = [
        "🎉 Ganaste un profit extra!",
        "🆕 Nuevo cliente conseguido!",
        "💡 Bonus estratégico desbloqueado!",
        "🍖 Te ganaste un asado virtual!",
        "🔄 Sin premio, intenta otra vez"
    ]
    placeholder = st.empty()
    # Animación fake de giro
    for i in range(10):
        premio_fake = random.choice(premios)
        placeholder.markdown(f"🎡 Ruleta gira... {premio_fake}")
        time.sleep(0.2)
    premio_final = random.choice(premios)
    placeholder.markdown(f"🎡 ¡La ruleta se detuvo en... {premio_final}!")
    st.balloons()
    st.success(premio_final)

# ---- Mostrar cliente actual ----
if st.session_state.ronda < len(clients):
    client = clients[st.session_state.ronda]
    st.subheader(f"Cliente: {client['nombre']}")
    st.markdown(f"**Relación con C-Level:** {client['relacion'].capitalize()}")
    st.markdown(f"**Potencial de ingresos:** ${client['potencial']:,}")

    strategies = {
        "Priorizar atención y presentar demo personalizada 🎯": 1.0,
        "Negociar descuento estratégico 💼": 0.7,
        "Ignorar objeciones y cerrar rápido ⚡": 0.3
    }

    decision = st.radio("Elige tu estrategia:", list(strategies.keys()), index=0)

    if st.button("Enviar decisión"):
        factor = strategies[decision]
        impacto = client["potencial"] * factor
        st.session_state.impacto_total += impacto
        st.session_state.historial.append({
            "Cuenta": client["nombre"],
            "Estrategia": decision,
            "Impacto": impacto,
            "Semaforo": semaforo(factor)
        })
        st.success(f"{semaforo(factor)} - Impacto generado: ${impacto:,.0f}")
        st.session_state.ronda += 1
        st.experimental_rerun()

# ---- Juego terminado ----
else:
    st.markdown("### 🚀 ¡Reto completado!")
    st.markdown(f"**Impacto total generado:** ${st.session_state.impacto_total:,.0f}")

    # ---- Tabla resumen ----
    df = pd.DataFrame(st.session_state.historial)
    st.markdown("### Resumen de decisiones")
    st.table(df)

    # ---- Gráfico divertido ----
    fig, ax = plt.subplots(figsize=(8,5))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#8c564b']
    bars = ax.bar(df["Cuenta"], df["Impacto"], color=colors)
    ax.set_ylabel("Impacto ($)")
    ax.set_title("Impacto por Cliente")
    for i, bar in enumerate(bars):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height(),
                f"${int(bar.get_height()):,}\n{df['Semaforo'][i]}",
                ha='center', va='bottom', fontsize=10)
    st.pyplot(fig)

    # ---- Ruleta de premios ----
    st.markdown("### 🎡 Ruleta de premios")
    if st.button("Girar ruleta"):
        ruleta_premio()

    st.markdown("""
    🎯 **Has demostrado tu habilidad estratégica en ventas B2B**  
    💡 Comparte tu resultado en LinkedIn y muestra tu perfil profesional.
    """)

    if st.button("Volver a jugar"):
        st.session_state.ronda = 0
        st.session_state.impacto_total = 0
        st.session_state.historial = []
        st.experimental_rerun()
