import streamlit as st
from config import SECTIONS


def render_sidebar():
    with st.sidebar:
        st.markdown("## EU27")
        for chapter, subsections in SECTIONS.items():
            st.markdown(
                f'<div class="chapter-box">{chapter}</div>',
                unsafe_allow_html=True
            )
            for sub in subsections:
                if st.button(sub, key=sub, use_container_width=True):
                    st.session_state.active_section = sub
                    st.session_state.show_table = False
