# sections/buildings.py

import streamlit as st
from config import COLORS

def render(df):
    st.title("🏠 Buildings Electrification")
    st.markdown("---")

    st.markdown("""
    Electrification of buildings focuses on replacing gas boilers with 
    **heat pumps** and improving energy efficiency through retrofitting.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Key Metrics")
        st.metric("Heat Pump Installations (2023)", "3.2M units", "+15%")
        st.metric("Share of Electric Heating", "12%", "+2%")
        st.metric("Buildings Retrofitted", "1.1M", "+8%")

    with col2:
        st.subheader("2030 Targets")
        st.progress(12, text="Heat Pump Share — Target: 30%")
        st.progress(22, text="Retrofit Rate — Target: 50%")
        st.progress(8, text="Zero-Emission New Buildings — Target: 100%")

    st.markdown("---")
    st.subheader("Barriers & Enablers")
    st.markdown("""
    - 💰 **Upfront costs** remain the biggest barrier
    - 🔧 **Skilled workforce** shortage slowing installation
    - ✅ **EU subsidy schemes** driving adoption in Nordic countries
    """)
