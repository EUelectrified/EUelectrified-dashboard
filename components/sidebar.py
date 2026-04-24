import re

import streamlit as st
from config import OVERVIEW_ONLY, SECTIONS


def _key_slug(text: str) -> str:
    return re.sub(r"[^0-9a-zA-Z]+", "_", text).strip("_")


def render_sidebar():
    with st.sidebar:
        st.markdown("## EU27")
        current = st.session_state.get("active_section")
        first = next(iter(SECTIONS))
        nav = {first: SECTIONS[first]} if OVERVIEW_ONLY else SECTIONS
        for chapter, subsections in nav.items():
            st.markdown(
                f'<div class="chapter-box">{chapter}</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="sidebar-chapter-pad" aria-hidden="true"></div>',
                unsafe_allow_html=True,
            )
            for subsection in subsections:
                is_active = subsection == current
                key = f"nav_{_key_slug(chapter)}__{_key_slug(subsection)}"
                # All rows use the same control so text aligns; active = disabled (styled in CSS)
                if is_active:
                    st.button(
                        subsection,
                        key=key,
                        use_container_width=True,
                        disabled=True,
                    )
                else:
                    if st.button(
                        subsection,
                        key=key,
                        use_container_width=True,
                    ):
                        st.session_state.active_section = subsection
                        st.session_state.show_table = False
