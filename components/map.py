import streamlit as st
import plotly.express as px


def render_map(df, graphic_title: str | None = None):
    # Use an OPAQUE color to avoid slight mismatches from alpha blending.
    panel_bg = "#dde2e9"  # slightly darker light grey
    z_min = float(df["value"].min())
    z_max = float(df["value"].max())
    # Stable, readable ticks (5 steps) without overfitting to the dummy data
    ticks = [round(z_min + (z_max - z_min) * i / 4, 1) for i in range(5)]
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
        hovertemplate="<b>%{hovertext}</b>: %{z:.1f}%<extra></extra>",
        marker_line_color="rgba(60,60,60,0.55)",
        marker_line_width=0.7,
    )
    fig.update_geos(
        visible=False,
        resolution=50,
        # Don't draw surrounding geography outlines (non‑EU countries)
        showcoastlines=False,
        showland=True,
        landcolor=panel_bg,
        showframe=False,
        # "Melts" into the chart panel (not into the page)
        bgcolor=panel_bg,
        # Manual framing tends to be more predictable than fitbounds for choropleths
        # and avoids the "zoomed out" look from overly-wide bounds.
        lonaxis_range=[-22, 47],
        lataxis_range=[32, 74],
        center=dict(lon=15, lat=54),
        projection_scale=1.30,
    )
    fig.update_layout(
        # (Width is controlled by Streamlit via use_container_width=True.)
        # Reduce height so the map reads wider (closer to ~16:9).
        height=460,
        # Keep a small top margin for the in-chart banner only.
        # Reserve a SMALL right margin for the colorbar so the chart has clear edges.
        margin=dict(l=0, r=2, t=44 if graphic_title else 0, b=0),
        paper_bgcolor=panel_bg,
        plot_bgcolor=panel_bg,
        coloraxis_colorbar=dict(
            title=dict(
                text="Elec %",
                font=dict(color="rgba(0,0,0,0.65)", size=13),
            ),
            len=0.62,
            y=0.5,
            # Place colorbar close to the map, inside the reserved margin
            x=0.895,
            xanchor="left",
            xpad=0,
            thickness=12,
            bgcolor=panel_bg,
            tickvals=ticks,
            tickformat=".1f",
            tickfont=dict(color="rgba(0,0,0,0.65)", size=12),
        ),
    )

    # Ensure geo background exactly matches the panel background everywhere.
    fig.update_layout(geo=dict(bgcolor=panel_bg, landcolor=panel_bg))

    # Give the full chart panel a subtle edge so it "ends" cleanly on the page.
    # Border only (no fill) to avoid any double-layer shading differences.
    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=0,
        x1=1,
        y0=0,
        y1=1,
        line=dict(color="rgba(0,0,0,0.12)", width=1),
        fillcolor="rgba(0,0,0,0)",
        layer="above",
    )

    # Let the map use the full plot width; the colorbar lives in the right margin.
    fig.update_geos(domain=dict(x=[0.0, 1.0], y=[0.0, 1.0]))

    if graphic_title:
        # Title positioned in the top margin area (paper coords allow >1.0).
        # This avoids layout.title's y∈[0,1] restriction and lets us center vertically.
        fig.add_annotation(
            text=f"<b>{graphic_title}</b>",
            x=0.0,
            y=1.045,
            xref="paper",
            yref="paper",
            xanchor="left",
            yanchor="middle",
            showarrow=False,
            align="left",
            font=dict(size=18, color="rgba(0,0,0,0.80)"),
        )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def render_table(df):
    st.dataframe(
        df[["country", "value"]]
        .rename(columns={"country": "Country", "value": "Value (%)"})
        .sort_values("Value (%)", ascending=False)
        .reset_index(drop=True),
        use_container_width=True,
        height=480,
    )
