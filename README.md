# Solar Data Challenge – Week 0
**Author:** Habtamu Wendifraw  
**Course:** 10x Academy - Data Challenge  
**Date:** November 2025  

---

## 🌞 Project Overview
This project analyzes solar energy production data across multiple countries to explore patterns, trends, and relationships between solar power output and other variables.  
The goal was to use Python for data cleaning, visualization, and insights generation.

---

## 📁 Folder Structure
solar-challenge-week0/
│
├── data/ # Raw and cleaned CSV files (not uploaded due to .gitignore)
├── notebooks/ # Jupyter notebooks for analysis
│ ├── solar_analysis.ipynb
├── app/ # Streamlit dashboard
│ ├── main.py
│ ├── utils.py
├── reports/ # PDFs, charts, interim report
│ ├── Solar_Data_Challenge_Interim_Report.pdf
└── README.md # This file


---

## ⚙️ Technologies Used
- **Python** (pandas, matplotlib, seaborn)
- **Streamlit** (for dashboard)
- **GitHub** (for version control)
- **Google Colab / Jupyter Notebook** (for development)

---

## 🧹 Data Preparation
- Loaded and cleaned solar dataset (handled missing values and removed duplicates)
- Converted date columns to proper datetime format
- Added summary statistics and new columns for analysis

---

## 📊 Visualizations
1. Line chart showing solar energy output by country  
2. Boxplot comparing solar intensity across regions  
3. Correlation heatmap between numeric features  

---

## 🖥️ Streamlit Dashboard
An interactive dashboard was built using **Streamlit** that allows:
- CSV upload via `st.file_uploader`
- Dynamic visualizations (line, box, bar charts)
- Country-based filtering

**Public App:** [Streamlit App URL goes here once deployed]  
**Repository:** [https://github.com/Habtu32/solar-challenge-week0](https://github.com/Habtu32/solar-challenge-week0)

---

## 📈 Key Insights
- Country A and Country B showed higher average production than others.  
- Seasonal variations strongly affect solar intensity trends.  
- The dataset provides a good foundation for predictive modeling in future tasks.

---

## 🕒 Time Management Reflection
To balance this project with full-time work and my MSIT course:
- I used the **Eisenhower Matrix** and **Time Blocking** (Google Calendar)
- Focused on high-priority tasks during early mornings and weekends
- Allocated short review sessions each evening

---

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Habtu32/solar-challenge-week0.git
   cd solar-challenge-week0/app

## Install dependencies:

pip install -r requirements.txt

## Run Streamlit app:

streamlit run main.py

📬 Contact
Habtamu Wendifraw
📧 habtuwendifraw@gmail.com