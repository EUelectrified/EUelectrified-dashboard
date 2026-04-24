# sections/transport.py

import streamlit as st
from config import COLORS

def render(df):
    st.title("🚗 Transport Electrification")
    st.markdown("---")

    st.markdown("""
    Transport electrification covers **electric vehicles (EVs)**, 
    charging infrastructure, and the phase-out of internal combustion engines.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Key Metrics")
        st.metric("EV Share of New Car Sales (2023)", "21%", "+5%")
        st.metric("Total EVs on Road (EU27)", "8.4M", "+32%")
        st.metric("Public Charging Points", "620K", "+28%")

    with col2:
        st.subheader("2030 Targets")
        st.progress(21, text="EV Share of New Sales — Target: 60%")
        st.progress(14, text="Charging Infrastructure — Target: 100%")
        st.progress(9, text="Electric Buses & Trucks — Target: 40%")

    st.markdown("---")
    st.subheader("Barriers & Enablers")
    st.markdown("""
    - 🔋 **Battery costs** still high for commercial vehicles
    - ⚡ **Charging network gaps** in Eastern Europe
    - ✅ **2035 ICE ban** creating strong market signal
    - ✅ **Purchase incentives** boosting EV adoption in France & Germany
    """)
