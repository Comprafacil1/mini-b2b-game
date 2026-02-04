# b2b_game_premium_final.py
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

# ---- Branding premium ----
st.markdown("""
<div style='display:flex; justify-content:space-between; align-items:center'>
<h1 style='color:#4B0082;'>🎯 Mini B2B Sales Challenge - Modo Killer</h1>
<span style='font-size:18px; font-weight:bold'>@Monik</span>
</div>
<p style='font-size:18px;'>Toma decisiones

