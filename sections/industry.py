# sections/industry.py

import streamlit as st
from config import COLORS

def render(df):
    st.title("🏭 Industry Electrification")
    st.markdown("---")

    st.markdown("""
    Industrial electrification targets **hard-to-abate sectors** such as 
    steel, cement, and chemicals — replacing fossil fuels with electricity 
    and green hydrogen.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Key Metrics")
        st.metric("Industrial Electrification Rate (2023)", "8%", "+1%")
        st.metric("Electric Arc Furnace Steel Share", "40%", "+3%")
        st.metric("Industrial Heat Pumps Installed", "18K units", "+22%")

    with col2:
        st.subheader("2030 Targets")
        st.progress(8, text="Overall Electrification Rate — Target: 25%")
        st.progress(40, text="Electric Steel Production — Target: 70%")
        st.progress(5, text="Green Hydrogen in Industry — Target: 20%")

    st.markdown("---")
    st.subheader("Barriers & Enablers")
    st.markdown("""
    - 🌡️ **High-temperature processes** difficult to electrify
    - 💸 **Carbon pricing** not yet high enough to drive switching
    - ✅ **EU Industrial Policy** supporting green steel investments
    - ✅ **Hydrogen valleys** emerging in Germany, Netherlands & Spain
    """)
