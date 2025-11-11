# app/main.py

# ---------------------------------------------
# 📊 Solar Data Cross-Country Dashboard
# Author: Habtamu Wendifraw
# ---------------------------------------------

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------
# 🌞 Page Setup
# ---------------------------------------------
st.set_page_config(page_title="Solar Data Comparison", layout="wide")
st.title("☀️ Cross-Country Solar Data Dashboard")
st.markdown("""
This app allows you to **compare solar metrics** (GHI, DNI, DHI) across **Benin**, **Sierra Leone**, and **Togo**.  
Upload your cleaned datasets below to get started.
""")

# ---------------------------------------------
# 📂 Upload Cleaned CSVs
# ---------------------------------------------
st.sidebar.header("🔽 Upload Cleaned Data Files")

benin_file = st.sidebar.file_uploader("Upload Benin CSV", type="csv")
sierra_file = st.sidebar.file_uploader("Upload Sierra Leone CSV", type="csv")
togo_file = st.sidebar.file_uploader("Upload Togo CSV", type="csv")

# ---------------------------------------------
# 🧹 Load Data
# ---------------------------------------------
if benin_file and sierra_file and togo_file:
    benin = pd.read_csv(benin_file)
    sierra = pd.read_csv(sierra_file)
    togo = pd.read_csv(togo_file)

    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"

    # Combine into one dataframe
    data = pd.concat([benin, sierra, togo], ignore_index=True)

    # ---------------------------------------------
    # 🎛 Sidebar Options
    # ---------------------------------------------
    st.sidebar.header("⚙️ Filter and Visualization Options")

    selected_countries = st.sidebar.multiselect(
        "Select countries to display:",
        ["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )

    selected_metric = st.sidebar.selectbox(
        "Select solar metric:",
        ["GHI", "DNI", "DHI"]
    )

    # Filter by country
    data_filtered = data[data["Country"].isin(selected_countries)]

    # ---------------------------------------------
    # 🎚 Filter by Value Range
    # ---------------------------------------------
    st.sidebar.subheader("📈 Filter by Value Range")
    value_range = st.sidebar.slider(
        f"Select {selected_metric} range",
        float(data_filtered[selected_metric].min()),
        float(data_filtered[selected_metric].max()),
        (
            float(data_filtered[selected_metric].min()),
            float(data_filtered[selected_metric].max())
        )
    )

    data_filtered = data_filtered[
        (data_filtered[selected_metric] >= value_range[0]) &
        (data_filtered[selected_metric] <= value_range[1])
    ]

    # ---------------------------------------------
    # 📊 Boxplot
    # ---------------------------------------------
    st.subheader(f"{selected_metric} Distribution by Country")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Country", y=selected_metric, data=data_filtered, palette="Set2", ax=ax)
    ax.set_title(f"{selected_metric} Comparison Across Countries", fontsize=14)
    st.pyplot(fig)

    # ---------------------------------------------
    # 📋 Summary Table
    # ---------------------------------------------
    st.subheader(f"Summary Statistics for {selected_metric}")
    summary = (
        data_filtered.groupby("Country")[[selected_metric]]
        .agg(["mean", "median", "std"])
        .round(3)
    )
    st.dataframe(summary)

    # ---------------------------------------------
    # 📈 Average Metric Bar Chart
    # ---------------------------------------------
    st.subheader(f"Average {selected_metric} by Country")
    avg_metric = data_filtered.groupby("Country")[selected_metric].mean().round(2)
    st.bar_chart(avg_metric)

    # ---------------------------------------------
    # 🧠 Key Insights
    # ---------------------------------------------
    st.subheader("🧠 Observations")
    st.markdown("""
    - Countries with higher **GHI** (Global Horizontal Irradiance) tend to have stronger solar potential.  
    - Comparing **median values** gives a better idea of consistency across regions.  
    - The **variability** (standard deviation) can help identify stable vs. fluctuating solar regions.
    """)

else:
    st.warning("⚠️ Please upload all three cleaned CSV files (Benin, Sierra Leone, and Togo) to continue.")
