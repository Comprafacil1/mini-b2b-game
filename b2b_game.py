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
        background-image: url('https://www.wallpaperflare.com/static/115/660/246/business-computer-finance-photo.jpg'); /* Imagen premium para el fondo */
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
                    st.session_state.impacto_total += impacto
        else:
            # Mostrar resultados ya tomados
            st.markdown(f"**Estrategia elegida:** {st.session_state.historial.loc[i, 'Estrategia']}")
            st.markdown(f"**Impacto:** ${st.session_state.historial.loc[i, 'Impacto']:,}")
            st.markdown(f"**Semáforo:** {st.session_state.historial.loc[i, 'Semaforo']}")

# ---- Gráfico de barras dinámico ----
st.markdown("---")
st.markdown("### Impacto por cliente")
# Crear un DataFrame con el impacto de cada cliente
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
    
    # Hacer la ruleta más destacada y grande
    st.markdown("""
    <div style="text-align: center; font-size: 36px; font-weight: bold; color: #FF5733; padding: 20px;">
        🎡 **Ruleta de premios** (¡Haz clic para girar!)
    </div>
    """, unsafe_allow_html=True)

    if "ruleta_girada" not in st.session_state:
        st.session_state.ruleta_girada = False

    # Botón grande para girar la ruleta (y eliminar el botón pequeño)
    if not st.session_state.ruleta_girada and st.button("¡Girar la Ruleta!", key="girar_grande"):
        # Lista de premios
        premios = [
            "🍖 Te ganaste un asado virtual!",
            "🔄 Vuelve pronto",
            "💰 Te ganaste un profit",
            "🆕 Te ganaste un cliente"
        ]
        
        placeholder = st.empty()  # Creamos un espacio para mostrar la animación
        for _ in range(12):  # Simula que la ruleta está girando
            premio_fake = random.choice(premios)
            placeholder.markdown(f"🎡 Ruleta gira... {premio_fake}", unsafe_allow_html=True)
            time.sleep(0.15)  # Pausa para dar el efecto de rotación

        # Elegir un premio final aleatorio
        premio_final = random.choice(premios)
        placeholder.markdown(f"🎡 ¡La ruleta se detuvo en... {premio_final}!", unsafe_allow_html=True)
        st.balloons()  # Animación de confetti
        st.success(premio_final)
        st.session_state.ruleta_girada = True

    if st.button("Volver a jugar"):
        # Reiniciar el juego
        st.session_state.historial = pd.DataFrame({
            "Cuenta": [c["nombre"] for c in clients],
            "Estrategia": ["" for _ in clients],
            "Impacto": [0 for _ in clients],
            "Semaforo": ["" for _ in clients]
        })
        st.session_state.impacto_total = 0
        st.session_state.ruleta_girada = False
        st.experimental_rerun()
