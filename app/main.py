# app/main.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------
# Sidebar: User Inputs
# ------------------------------
st.sidebar.header("Select Countries and Metric")

# User can select which countries to display
selected_countries = st.sidebar.multiselect(
    "Choose countries:",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]  # all selected by default
)

# User can select which solar metric to visualize
selected_metric = st.sidebar.selectbox(
    "Choose metric:",
    ["GHI", "DNI", "DHI"]
)

# ------------------------------
# Page Title
# ------------------------------
st.title("Cross-Country Solar Data Dashboard")

# ------------------------------
# Load and Prepare Data
# ------------------------------
@st.cache_data  # Cache the data to speed up app
def load_data():
    # Read cleaned CSVs (local files)
    benin = pd.read_csv('../data/benin-malanville_clean.csv')
    sierra = pd.read_csv('../data/sierraleone-bumbuna_clean.csv')
    togo = pd.read_csv('../data/togo-dapaong_qc_clean.csv')
    
    # Add a column to identify the country
    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    
    # Combine all datasets into one
    return pd.concat([benin, sierra, togo], ignore_index=True)

# Load the data
data = load_data()

# Filter the data based on selected countries
data_filtered = data[data['Country'].isin(selected_countries)]

# ------------------------------
# Boxplot: Metric Comparison
# ------------------------------
st.subheader(f"{selected_metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Country', y=selected_metric, data=data_filtered, palette="Set2")
ax.set_title(f"{selected_metric} by Country")
st.pyplot(fig)

# ------------------------------
# Summary Table
# ------------------------------
st.subheader(f"Summary Statistics for {selected_metric}")
summary = data_filtered.groupby('Country')[[selected_metric]].agg(['mean','median','std'])
st.dataframe(summary)

# ------------------------------
# Optional Bar Chart: Average Metric
# ------------------------------
st.subheader(f"Average {selected_metric} by Country")
avg_metric = data_filtered.groupby('Country')[selected_metric].mean()
st.bar_chart(avg_metric)

# ------------------------------
# Optional: Filter by Value Slider
# ------------------------------
st.sidebar.subheader("Filter by Metric Range")
value_range = st.sidebar.slider(
    f"Select {selected_metric} range",
    float(data_filtered[selected_metric].min()),
    float(data_filtered[selected_metric].max()),
    (float(data_filtered[selected_metric].min()), float(data_filtered[selected_metric].max()))
)

# Apply filter
data_filtered = data_filtered[
    (data_filtered[selected_metric] >= value_range[0]) &
    (data_filtered[selected_metric] <= value_range[1])
]

st.sidebar.write(f"Showing {len(data_filtered)} rows after filtering")
