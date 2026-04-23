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
            # Use a single radio group per chapter for consistent spacing/indentation.
            current = st.session_state.get("active_section")
            try:
                index = subsections.index(current) if current in subsections else 0
            except ValueError:
                index = 0

            selected = st.radio(
                label=f"{chapter} subsections",
                options=subsections,
                index=index,
                key=f"nav_{chapter}",
                label_visibility="collapsed",
            )

            if selected != current:
                st.session_state.active_section = selected
                st.session_state.show_table = False
