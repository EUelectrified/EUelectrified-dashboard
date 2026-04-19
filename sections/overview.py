import streamlit as st
from components.map import render_map, render_table
from config import EU27_COUNTRIES


def render(df):
    # Give the map more horizontal room; keep side columns compact.
    col_main, col_keys, col_countries = st.columns([7.2, 1.5, 0.8])

    with col_main:
        st.markdown("### 1. EU27 – Summary")
        st.markdown(f"#### {st.session_state.active_section}")

        if st.session_state.show_table:
            render_table(df)
        else:
            render_map(df)

        st.markdown("<div style='margin-top:-14px'>", unsafe_allow_html=True)
        toggle_label = "↩ show map" if st.session_state.show_table else "⇄ show table"
        if st.button(toggle_label):
            st.session_state.show_table = not st.session_state.show_table
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='margin-top:0px'>", unsafe_allow_html=True)
        st.info(
            "The graph shows the share of electricity in the final energy consumption. "
            "In a climate-neutral scenario, the share would not rise to 100% for most "
            "countries as some processes are difficult to electrify. In some cases, "
            "Carbon Capture and Storage (CCS) is used to prevent residual emissions, "
            "in other instances negative emissions will be used."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_keys:
        st.markdown("### Key Numbers")
        eu_avg = df["value"].mean()
        st.metric("EU Average", f"{eu_avg:.1f} %")

        top3 = df.nlargest(3, "value")[["country", "value"]].reset_index(drop=True)
        st.markdown("**Top performers:**")
        for i, row in top3.iterrows():
            st.markdown(
                f"<div style='margin:0;line-height:1.4'>{i+1}. {row['country']} — {row['value']}%</div>",
                unsafe_allow_html=True
            )

        st.markdown("<div style='margin:6px 0'></div>", unsafe_allow_html=True)

        bottom3 = df.nsmallest(3, "value")[["country", "value"]].reset_index(drop=True)
        st.markdown("**Lowest:**")
        for i, row in bottom3.iterrows():
            st.markdown(
                f"<div style='margin:0;line-height:1.4'>{27-2+i}. {row['country']} — {row['value']}%</div>",
                unsafe_allow_html=True
            )

    with col_countries:
        st.markdown("### Country Deep Dives")
        country_links = "".join(
            f"<div style='line-height:1.5;font-size:0.85rem'>{c}</div>"
            for c in EU27_COUNTRIES
        )
        st.markdown(country_links, unsafe_allow_html=True)
