import re

import streamlit as st
from config import SECTIONS


def _key_slug(text: str) -> str:
    return re.sub(r"[^0-9a-zA-Z]+", "_", text).strip("_")


def render_sidebar():
    with st.sidebar:
        st.markdown("## EU27")
        current = st.session_state.get("active_section")
        for chapter, subsections in SECTIONS.items():
            st.markdown(
                f'<div class="chapter-box">{chapter}</div>',
                unsafe_allow_html=True
            )
            for subsection in subsections:
                is_active = subsection == current
                if is_active:
                    st.markdown(
                        f'<div class="nav-item-active">{subsection}</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    if st.button(
                        subsection,
                        key=f"nav_{_key_slug(chapter)}__{_key_slug(subsection)}",
                        use_container_width=True,
                    ):
                        st.session_state.active_section = subsection
                        st.session_state.show_table = False
