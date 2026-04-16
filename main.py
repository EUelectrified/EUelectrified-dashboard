import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EU Electrification Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv("data/eu27_dummy.csv")

sections = {
    "1. EU27 – Summary": [
        "1.1 Share of Elec of FEC",
        "1.2 Share of Elec in Transport",
        "1.3 Share of Elec in Buildings",
        "1.4 Share of Elec in Industry",
        "1.5 Clean Generation Share",
        "1.6 Wholesale Power Price",
        "1.7 Grids & Legislation",
    ],
    "2. Buildings": [
        "2.1 Elec Share in Buildings",
        "2.2 Heat Pump Adoption",
        "2.3 Building Renovation Rate",
        "2.4 Energy Efficiency Index",
    ],
    "3. Transport": [
        "3.1 EV Share of New Sales",
        "3.2 EV Stock Share",
        "3.3 Charging Infrastructure",
        "3.4 Public Transport Electrification",
    ],
    "4. Industry": [
        "4.1 Industrial Elec Share",
        "4.2 Green Hydrogen Capacity",
        "4.3 Electrolysis Deployment",
        "4.4 Emissions Intensity",
    ],
}

eu27_countries = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
    "Czechia", "Denmark", "Estonia", "Finland", "France",
    "Germany", "Greece", "Hungary", "Ireland", "Italy",
    "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands",
    "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
    "Spain", "Sweden"
]

if "active_section" not in st.session_state:
    st.session_state.active_section = "1.1 Share of Elec of FEC"
if "show_table" not in st.session_state:
    st.session_state.show_table = False

# ─── GLOBAL CSS ────────────────────────────────────────────────
st.markdown("""
<style>
/* Remove all button borders/boxes */
.stButton > button {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    padding: 2px 8px !important;
    margin: 0px !important;
    font-size: 0.85rem !important;
    height: auto !important;
    text-align: left !important;
    color: inherit !important;
}
.stButton > button:hover {
    background-color: rgba(255,255,255,0.1) !important;
    border: none !important;
}
/* Remove metric box borders */
[data-testid="metric-container"] {
    border: none !important;
    box-shadow: none !important;
    background: none !important;
    padding: 0 !important;
}
/* Tighten main content top padding */
.block-container {
    padding-top: 1.5rem !important;
}
/* Sidebar chapter headers */
.chapter-box {
    background-color: #1f3a5f;
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    margin-top: 8px;
    margin-bottom: 2px;
    font-weight: bold;
    font-size: 0.9rem;
}
/* Remove stMarkdown element borders if any */
.stMarkdown h3 {
    border: none !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

# ─── LEFT SIDEBAR ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## EU27")
    for chapter, subsections in sections.items():
        st.markdown(f'<div class="chapter-box">{chapter}</div>', unsafe_allow_html=True)
        for sub in subsections:
            if st.button(sub, key=sub, use_container_width=True):
                st.session_state.active_section = sub
                st.session_state.show_table = False

# ─── MAIN LAYOUT ───────────────────────────────────────────────
col_main, col_keys, col_countries = st.columns([5, 2, 1.2])

with col_main:
    st.markdown("### 1. EU27 – Summary")
    st.markdown(f"#### {st.session_state.active_section}")

    if st.session_state.show_table:
        st.dataframe(
    df[["country", "value"]].rename(
        columns={"country": "Country", "value": "Value (%)"}
    ).sort_values("Value (%)", ascending=False).reset_index(drop=True),
    width='stretch',
    height=480
)
    else:
        fig = px.choropleth(
            df,
            locations="iso_alpha3",
            color="value",
            hover_name="country",
            hover_data={"value": ":.1f", "iso_alpha3": False},
            color_continuous_scale="Blues",
            scope="europe",
        )
        fig.update_traces(
            hovertemplate="<b>%{hovertext}</b>: %{z:.1f}%<extra></extra>"
        )
        fig.update_geos(
            visible=False,
            resolution=50,
            showcoastlines=True,
            coastlinecolor="lightgrey",
            showland=True,
            landcolor="whitesmoke",
            showframe=False,
            lonaxis_range=[-25, 45],
            lataxis_range=[34, 72],
        )
        fig.update_layout(
            height=550,
            margin=dict(l=0, r=0, t=0, b=0),
            coloraxis_colorbar=dict(title="Elec %"),
        )
        st.plotly_chart(fig, width='stretch', config={"displayModeBar": False})

    # Toggle button — flush below map
    st.markdown("<div style='margin-top:-10px'>", unsafe_allow_html=True)
    toggle_label = "↩ show map" if st.session_state.show_table else "⇄ show table"
    if st.button(toggle_label):
        st.session_state.show_table = not st.session_state.show_table
    st.markdown("</div>", unsafe_allow_html=True)

    # Info box — tight below toggle
    st.markdown("<div style='margin-top:4px'>", unsafe_allow_html=True)
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
        st.markdown(f"<div style='margin:0;line-height:1.4'>{i+1}. {row['country']} — {row['value']}%</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin:6px 0'></div>", unsafe_allow_html=True)

    bottom3 = df.nsmallest(3, "value")[["country", "value"]].reset_index(drop=True)
    st.markdown("**Lowest:**")
    for i, row in bottom3.iterrows():
        st.markdown(f"<div style='margin:0;line-height:1.4'>{27-2+i}. {row['country']} — {row['value']}%</div>", unsafe_allow_html=True)

with col_countries:
    st.markdown("### Country Deep Dives")
    country_links = "".join(
        f"<div style='line-height:1.5;font-size:0.85rem'>{c}</div>"
        for c in eu27_countries
    )
    st.markdown(country_links, unsafe_allow_html=True)
