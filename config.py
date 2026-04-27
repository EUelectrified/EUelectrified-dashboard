import os

# Set env `EU_DASHBOARD_OVERVIEW_ONLY=1` (or "true") while tuning the overview: sidebar
# shows only section 1, and other section modules are not loaded in main. Omit for the full app.
def _read_overview_only() -> bool:
    v = os.environ.get("EU_DASHBOARD_OVERVIEW_ONLY", "").strip().lower()
    return v in ("1", "true", "yes")


OVERVIEW_ONLY = _read_overview_only()

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
    width: 285px !important;
}
section[data-testid="stSidebar"] > div {
    width: 285px !important;
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

/* Sidebar: aggressively remove default vertical padding inside wrappers */
section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

/* Sidebar: very tight row gap between subsection controls */
section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
    row-gap: 0 !important;
    gap: 0 !important;
}

/* Button reset is for the sidebar nav only (never global) */
section[data-testid="stSidebar"] .stButton > button {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    padding: 1px 8px 1px 18px !important;
    margin: 0px !important;
    font-size: 0.78rem !important;
    line-height: 1.15 !important;
    height: auto !important;
    text-align: left !important;
    color: inherit !important;
}

/* Smaller headings for the compact right-side columns */
.right-col-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin: 0 0 0.25rem 0;
    line-height: 1.2;
}

/* Sidebar: subsection nav — one control type (button) for alignment; keep on one line */
section[data-testid="stSidebar"] .stButton {
    width: 100% !important;
    min-width: 0 !important;
    margin-left: 0 !important;
}
/* Same text box for enabled + disabled (avoids 1.1 / 1.2 walking sideways) */
section[data-testid="stSidebar"] .stButton > button,
section[data-testid="stSidebar"] .stButton > button:disabled,
section[data-testid="stSidebar"] .stButton > button[disabled] {
    font-size: 0.72rem !important;
    line-height: 1.3 !important;
    min-height: 1.5rem !important;
    width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
    padding: 1px 8px 1px 14px !important;
    text-align: left !important;
    margin-left: 0 !important;
    /* Streamlit buttons default to flex + centered label; all rows must start at the same x */
    display: flex !important;
    flex-direction: row !important;
    justify-content: flex-start !important;
    align-items: center !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
section[data-testid="stSidebar"] .stButton > button > p,
section[data-testid="stSidebar"] .stButton > button > span {
    text-align: left !important;
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 !important;
}
/* Streamlit may wrap the label in a direct child div; keep content flush left */
section[data-testid="stSidebar"] .stButton > button > div {
    display: flex !important;
    flex-direction: row !important;
    justify-content: flex-start !important;
    align-items: center !important;
    text-align: left !important;
    width: 100% !important;
    min-width: 0 !important;
    margin: 0 !important;
}
section[data-testid="stSidebar"] .stButton > button {
    font-weight: 400 !important;
}
/* Active row: some themes need weight on the label node, not just the <button> */
section[data-testid="stSidebar"] .stButton > button:disabled,
section[data-testid="stSidebar"] .stButton > button[disabled] {
    opacity: 1 !important;
    -webkit-text-fill-color: currentColor !important;
    font-weight: 700 !important;
    color: inherit !important;
    cursor: default !important;
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}
section[data-testid="stSidebar"] .stButton > button:disabled *,
section[data-testid="stSidebar"] .stButton > button[disabled] * {
    font-weight: 700 !important;
    opacity: 1 !important;
    -webkit-text-fill-color: currentColor !important;
    color: inherit !important;
}

/* Some Streamlit themes wrap the label; keep one left edge and single line */
section[data-testid="stSidebar"] .stButton > button * {
    white-space: nowrap !important;
    text-align: left !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
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
    /* Avoid content being clipped under Streamlit's top chrome */
    padding-top: 2.6rem !important;
    /* Reduce the gap between sidebar and main content */
    padding-left: 1.1rem !important;
    padding-right: 1.1rem !important;
}
.chapter-and-gap {
    display: block;
    width: 100%;
    vertical-align: top;
}
/* Gap lives here (not on empty streamlit block that may collapse) */
section[data-testid="stSidebar"] .chapter-and-gap .chapter-box {
    margin-top: 4px;
    margin-bottom: 0 !important;
}
.chapter-box {
    background-color: #1f3a5f;
    color: white;
    padding: 4px 8px 6px 8px;
    border-radius: 4px;
    margin-top: 4px;
    margin-bottom: 0.25rem;
    font-weight: 700;
    font-size: 1.05rem;
    line-height: 1.25;
}
section[data-testid="stSidebar"] .chapter-and-gap .sidebar-chapter-pad,
div.sidebar-chapter-pad {
    display: block;
    width: 100%;
    min-height: 0.65rem;
    height: 0.65rem;
    line-height: 0.65rem;
    font-size: 0.65rem;
    margin: 0.15rem 0 0.2rem 0;
    padding: 0;
    flex-shrink: 0;
    box-sizing: border-box;
    overflow: hidden;
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

.overview-map-stack div[data-testid="stPlotlyChart"] {
    margin-bottom: 0 !important;
}

/* Overview: map → toggle → info should feel like one block */
.overview-map-stack div[data-testid="stButton"] {
    margin-top: -28px !important;
}
.overview-map-stack div[data-testid="stButton"] button {
    /* Light mode: a real light “pill” */
    background-color: rgba(0, 0, 0, 0.06) !important;
    border: 1px solid rgba(0, 0, 0, 0.10) !important;
    border-radius: 10px !important;
    padding: 6px 10px !important;
    box-shadow: none !important;
}
.overview-map-stack div[data-testid="stButton"] button:hover {
    background-color: rgba(0, 0, 0, 0.09) !important;
    border-color: rgba(0, 0, 0, 0.12) !important;
}

@media (prefers-color-scheme: dark) {
    /* Dark mode: the previous “light black” read as invisible; use a light surface */
    .overview-map-stack div[data-testid="stButton"] button {
        background-color: rgba(255, 255, 255, 0.10) !important;
        border-color: rgba(255, 255, 255, 0.16) !important;
        color: rgba(255, 255, 255, 0.92) !important;
    }
    .overview-map-stack div[data-testid="stButton"] button:hover {
        background-color: rgba(255, 255, 255, 0.14) !important;
        border-color: rgba(255, 255, 255, 0.20) !important;
    }
}

.overview-info-box {
    width: 100% !important;
    max-width: none !important;
    box-sizing: border-box !important;
    margin-top: 0.0rem !important;
    padding: 0.7rem 0.9rem !important;
    border-radius: 10px !important;
    line-height: 1.45 !important;
    font-size: 0.95rem !important;
    /* Light mode: neutral grey surface */
    background: rgba(0, 0, 0, 0.06) !important;
    border: 1px solid rgba(0, 0, 0, 0.10) !important;
    color: var(--text-color, rgba(0, 0, 0, 0.86)) !important;
}

.overview-map-stack [data-testid="stMarkdownContainer"] .overview-info-box {
    display: block !important;
    width: 100% !important;
}

@media (prefers-color-scheme: dark) {
    .overview-info-box {
        /* Dark mode: light grey (not the Streamlit “info” blue) */
        background: rgba(255, 255, 255, 0.10) !important;
        border: 1px solid rgba(255, 255, 255, 0.16) !important;
        color: rgba(255, 255, 255, 0.92) !important;
    }
}

.stMarkdown h3 {
    border: none !important;
    box-shadow: none !important;
}

/* Overview: titles + map (single page block — pull map up under header) */
.overview-page-titles h3,
.overview-page-titles h4 {
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}
.overview-page-titles h3 {
    /* Theme-safe: visible in both light and dark mode */
    color: var(--text-color, rgba(0,0,0,0.95)) !important;
    font-size: 1.35rem;
    font-weight: 600;
    margin: 0 0 0.15rem 0 !important;
    line-height: 1.2;
}
.overview-page-titles h4 {
    color: var(--text-color, rgba(0,0,0,0.85)) !important;
    opacity: 0.85;
    font-size: 1.05rem;
    font-weight: 500;
    margin: 0 0 0.1rem 0 !important;
    line-height: 1.2;
}
/* No negative margin — that overlapped the map row, hid titles, and clipped the sub-header */
.overview-page-titles {
    margin: 0.15rem 0 0.12rem 0 !important;
    padding: 0 !important;
    overflow: visible !important;
    position: relative;
    z-index: 5;
}

/* Dark mode: ensure overview titles stay readable */
@media (prefers-color-scheme: dark) {
    .overview-page-titles h3 {
        color: rgba(255,255,255,0.95) !important;
    }
    .overview-page-titles h4 {
        color: rgba(255,255,255,0.88) !important;
        opacity: 1;
    }
}
</style>
"""

COLORS = {
    "primary": "#1f3a5f",
    "positive": "#2ecc71",
    "negative": "#e74c3c",
    "neutral": "#95a5a6",
}
