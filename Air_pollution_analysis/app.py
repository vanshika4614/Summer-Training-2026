import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Air Pollution Analysis Dashboard",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("AQI-INDIA.csv")


# -----------------------------
# Load CSS
# -----------------------------

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# -----------------------------
# Title
# -----------------------------

st.title("🌍 Air Pollution Analysis Dashboard")

st.write(
    """
This project analyses air pollution data from different cities and stations.
It provides dataset exploration, statistical analysis and interactive
visualizations of different pollutants.
"""
)


# -----------------------------
# Sidebar Navigation
# -----------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Dataset",
        "Data Analysis",
        "Visualizations",
        "About"
    ]
)


# ==========================================================
# DASHBOARD
# ==========================================================

if page == "Dashboard":

    st.header("📊 Dashboard")

    total_cities = df["city"].nunique()
    total_states = df["state"].nunique()
    total_records = len(df)
    total_pollutants = df["pollutant_id"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🏙 Cities", total_cities)
    col2.metric("🗺 States", total_states)
    col3.metric("📄 Records", total_records)
    col4.metric("🧪 Pollutants", total_pollutants)

    st.divider()

    st.subheader("📄 Dataset Preview")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    with col2:
        st.write("### Dataset Summary")

        st.write(f"**Rows:** {df.shape[0]}")
        st.write(f"**Columns:** {df.shape[1]}")
        st.write(f"**Cities:** {df['city'].nunique()}")
        st.write(f"**States:** {df['state'].nunique()}")
        st.write(f"**Pollutants:** {df['pollutant_id'].nunique()}")


# ==========================================================
# DATASET
# ==========================================================

elif page == "Dataset":

    st.header("📄 Dataset Explorer")

    st.write("Use the options below to explore the dataset.")

    search = st.text_input("Search City")

    pollutant = st.selectbox(
        "Select Pollutant",
        ["All"] + sorted(df["pollutant_id"].dropna().unique().tolist())
    )

    filtered_df = df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["city"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if pollutant != "All":
        filtered_df = filtered_df[
            filtered_df["pollutant_id"] == pollutant
        ]

    st.write(f"Showing **{len(filtered_df)} records**")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


# ==========================================================
# DATA ANALYSIS
# ==========================================================

elif page == "Data Analysis":

    st.header("📊 Data Analysis")

    st.subheader("Average Pollutant Level")

    pollutant_avg = (
        df.groupby("pollutant_id")["pollutant_avg"]
        .mean()
        .reset_index()
    )

    pollutant_avg["pollutant_avg"] = pollutant_avg[
        "pollutant_avg"
    ].round(2)

    st.dataframe(
        pollutant_avg,
        use_container_width=True
    )

    st.divider()

    st.subheader("Highest Average Pollutant")

    highest = pollutant_avg.loc[
        pollutant_avg["pollutant_avg"].idxmax()
    ]

    st.write(
        f"**{highest['pollutant_id']}** has the highest average "
        f"pollutant value of **{highest['pollutant_avg']}**."
    )

    st.divider()

    st.subheader("Missing Values")

    missing_values = df.isnull().sum().reset_index()

    missing_values.columns = [
        "Column",
        "Missing Values"
    ]

    st.dataframe(
        missing_values,
        use_container_width=True
    )

    st.divider()

    st.subheader("City-wise Record Count")

    city_count = (
        df.groupby("city")
        .size()
        .reset_index(name="Records")
        .sort_values("Records", ascending=False)
    )

    st.dataframe(
        city_count.head(20),
        use_container_width=True
    )


# ==========================================================
# VISUALIZATIONS
# ==========================================================

elif page == "Visualizations":

    st.header("📈 Data Visualizations")

    # Pollutant distribution
    fig1 = px.histogram(
        df,
        x="pollutant_avg",
        color="pollutant_id",
        title="Pollutant Value Distribution",
        labels={
            "pollutant_avg": "Average Pollutant Value",
            "pollutant_id": "Pollutant"
        }
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # Average pollutant levels
    pollutant_avg = (
        df.groupby("pollutant_id")["pollutant_avg"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        pollutant_avg,
        x="pollutant_id",
        y="pollutant_avg",
        color="pollutant_id",
        title="Average Level of Each Pollutant",
        labels={
            "pollutant_id": "Pollutant",
            "pollutant_avg": "Average Value"
        }
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # Number of records for each pollutant
    pollutant_count = (
        df["pollutant_id"]
        .value_counts()
        .reset_index()
    )

    pollutant_count.columns = [
        "Pollutant",
        "Records"
    ]

    fig3 = px.pie(
        pollutant_count,
        names="Pollutant",
        values="Records",
        title="Distribution of Pollutant Records"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # Top cities
    city_count = (
        df["city"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    city_count.columns = [
        "City",
        "Records"
    ]

    fig4 = px.bar(
        city_count,
        x="City",
        y="Records",
        title="Top 10 Cities by Number of Records"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )


# ==========================================================
# ABOUT
# ==========================================================

elif page == "About":

    st.header("ℹ️ About the Project")

    st.subheader("Project Objective")

    st.write(
        """
The objective of this project is to analyse air pollution data
collected from different cities and monitoring stations.
The dashboard provides an interactive way to explore pollutant
levels, identify patterns and understand the dataset using
Python-based data analysis and visualization.
"""
    )

    st.subheader("Technologies Used")

    st.write(
        """
        • Python
        • Pandas
        • Streamlit
        • Plotly
        • CSS
        """
    )

    st.subheader("Dataset")

    st.write(
        """
The dataset contains information about cities, states, monitoring
stations, update dates, pollutant types and pollutant measurements.
"""
    )

    st.subheader("Analysis Performed")

    st.write(
        """
        • Dataset exploration
        • Data filtering
        • Missing value analysis
        • Pollutant-wise analysis
        • City-wise analysis
        • Statistical summaries
        • Interactive data visualization
        """
    )


# -----------------------------
# Sidebar Information
# -----------------------------

st.sidebar.success("🌍 Air Pollution Dashboard")

st.sidebar.info(
    """
Python Data Analysis Project

✔ Pandas

✔ Streamlit

✔ Plotly

✔ Data Visualization
"""
)