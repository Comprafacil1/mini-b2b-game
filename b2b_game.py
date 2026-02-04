# b2b_game_killer.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time

# ---- Configuración de la página ----
st.set_page_config(page_title="🎯 Mini B2B Sales Challenge - Modo Killer", layout="wide")

# ---- Branding premium ----
st.markdown("<h1 style='text-align:center; color:#4B0082;'>🎯 Mini B2B Sales Challenge - Modo Killer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Demuestra tu capacidad de tomar decisiones estratégicas y maximizar impacto en ventas B2B.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---- Definir clientes/desafíos ----
clients = [
    {"nombre": "Cuenta A - Energía", "potencial": 500000, "relacion": "buena"},
    {"nombre": "Cuenta B - Minería", "potencial": 300000, "relacion": "media"},
    {"nombre": "Cuenta C - Tecnología", "potencial": 100000, "relacion": "baja"}
]

# ---- Inicializar estado de sesión ----
if "ronda" not in st.session_state:
    st.session_state["ronda"] = 0
if "impacto_total" not in st.session_state:
    st.session_state["impacto_total"] = 0
if "historial" not in st.session_state:
    st.session_state["historial"] = []

# ---- Mostrar cliente actual ----
if st.session_state["ronda"] < len(clients):
    client = clients[st.session_state["ronda"]]
    st.subheader(f"Cliente: {client['nombre']}")
    st.write(f"Relación con C-Level: **{client['relacion']}**")
    st.write(f"Potencial de ingresos: **${client['potencial']:,}**")

    # Opciones de estrategia
    strategies = {
        "Priorizar atención y presentar demo personalizada": 1.0,
        "Negociar descuento estratégico": 0.7,
        "Ignorar objeciones y cerrar rápido": 0.3
    }

    decision = st.radio("Elige tu estrategia:", list(strategies.keys()), key=client["nombre"])

    if st.button("Enviar decisión"):
        factor = strategies[decision]
        impacto = client["potencial"] * factor
        st.session_state["impacto_total"] += impacto
        st.session_state["historial"].append({
            "Cuenta": client["nombre"],
            "Estrategia": decision,
            "Impacto": impacto
        })
        st.success(f"Impacto generado en esta cuenta: ${impacto:,.0f}")
        st.session_state["ronda"] += 1
        st.experimental_rerun()

# ---- Juego terminado ----
else:
    st.markdown("### 🚀 ¡Reto completado!")
    st.markdown(f"**Impacto total generado:** ${st.session_state['impacto_total']:,.0f}")

    # ---- Tabla resumen ----
    df = pd.DataFrame(st.session_state["historial"])
    st.markdown("### Resumen de decisiones")
    st.table(df)

    # ---- Gráfico de impacto ----
    fig, ax = plt.subplots(figsize=(8,5))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    bars = ax.bar(df["Cuenta"], df["Impacto"], color=colors)
    ax.set_ylabel("Impacto ($)")
    ax.set_title("Impacto por Cliente")
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            f"${int(bar.get_height()):,}",
            ha='center', va='bottom', fontsize=10
        )
    st.pyplot(fig)

    # ---- Mensaje final premium ----
    st.markdown(
        """
        🎯 Has demostrado tu capacidad para tomar decisiones estratégicas en ventas B2B.  
        💡 Comparte tus resultados en LinkedIn y muestra tu perfil profesional.
        """
    )

    if st.button("Volver a jugar"):
        st.session_state["ronda"] = 0
        st.session_state["impacto_total"] = 0
        st.session_state["historial"] = []
        st.experimental_rerun()


