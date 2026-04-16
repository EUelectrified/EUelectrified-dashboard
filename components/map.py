import streamlit as st
import plotly.express as px


def render_map(df):
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
