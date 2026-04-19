SECTIONS = {
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

EU27_COUNTRIES = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
    "Czechia", "Denmark", "Estonia", "Finland", "France",
    "Germany", "Greece", "Hungary", "Ireland", "Italy",
    "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands",
    "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
    "Spain", "Sweden"
]

GLOBAL_CSS = """
<style>
/* Make the left sidebar narrower (more room for the map) */
section[data-testid="stSidebar"] {
    width: 250px !important;
}
section[data-testid="stSidebar"] > div {
    width: 250px !important;
}

/* Sidebar: tighter vertical rhythm */
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
}

/* Sidebar: remove extra spacing between blocks */
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] > * {
    margin-block-start: 0.15rem !important;
    margin-block-end: 0.15rem !important;
}
section[data-testid="stSidebar"] .stButton {
    margin: 0 !important;
    padding: 0 !important;
}
section[data-testid="stSidebar"] div[data-testid="stButton"] {
    margin: 0 !important;
    padding: 0 !important;
}
section[data-testid="stSidebar"] div[data-testid="stElementContainer"] {
    margin-bottom: 0.15rem !important;
}

.stButton > button {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    padding: 1px 8px !important;
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
[data-testid="metric-container"] {
    border: none !important;
    box-shadow: none !important;
    background: none !important;
    padding: 0 !important;
}
.block-container {
    padding-top: 1.5rem !important;
}
.chapter-box {
    background-color: #1f3a5f;
    color: white;
    padding: 3px 8px;
    border-radius: 4px;
    margin-top: 4px;
    margin-bottom: 1px;
    font-weight: bold;
    font-size: 0.9rem;
}

/* Reduce default spacing around info boxes */
div[data-testid="stAlert"] {
    padding: 0.6rem 0.8rem !important;
    margin: 0.25rem 0 0.25rem 0 !important;
}

/* Tighten spacing under Plotly charts */
div[data-testid="stPlotlyChart"] {
    margin-bottom: 0 !important;
}

.stMarkdown h3 {
    border: none !important;
    box-shadow: none !important;
}
</style>
"""

COLORS = {
    "primary": "#1f3a5f",
    "positive": "#2ecc71",
    "negative": "#e74c3c",
    "neutral": "#95a5a6",
}
