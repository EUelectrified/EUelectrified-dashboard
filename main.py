import pandas as pd
import streamlit as st

from components.sidebar import render_sidebar
from config import GLOBAL_CSS, OVERVIEW_ONLY, SECTIONS
from sections import overview

if not OVERVIEW_ONLY:
    from sections import buildings, industry, transport

st.set_page_config(
    page_title="EU Electrification Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

if "active_section" not in st.session_state:
    st.session_state.active_section = "1.1 Share of Elec of FEC"
if "show_table" not in st.session_state:
    st.session_state.show_table = False

df = pd.read_csv("data/eu27_dummy.csv")

if OVERVIEW_ONLY and not st.session_state["active_section"].startswith("1."):
    st.session_state["active_section"] = next(iter(SECTIONS.values()))[0]

render_sidebar()

section = st.session_state.active_section

if OVERVIEW_ONLY:
    overview.render(df)
else:
    if section.startswith("1."):
        overview.render(df)
    elif section.startswith("2."):
        buildings.render(df)
    elif section.startswith("3."):
        transport.render(df)
    elif section.startswith("4."):
        industry.render(df)

