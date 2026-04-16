import streamlit as st
import pandas as pd
from config import GLOBAL_CSS
from components.sidebar import render_sidebar
from sections import overview, buildings, transport, industry

st.set_page_config(
    page_title="EU Electrification Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

if "active_section" not in st.session_state:
    st.session_state.active_section = "1.1 Share of Elec of FEC"
if "show_table" not in st.session_state:
    st.session_state.show_table = False

df = pd.read_csv("data/eu27_dummy.csv")

render_sidebar()

section = st.session_state.active_section

if section.startswith("1."):
    overview.render(df)
elif section.startswith("2."):
    buildings.render(df)
elif section.startswith("3."):
    transport.render(df)
elif section.startswith("4."):
    industry.render(df)
