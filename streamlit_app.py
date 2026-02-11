## Step 00 - Import packages

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Diabetes Dashboard 🩺",
    layout="centered",
    page_icon="🩺",
)

## sidebar
st.sidebar.title("Diabetes Dataset Dashboard 🩺")
page = st.sidebar.selectbox("Select Page",["Introduction 📘","Visualization 📊"])

st.image("diabetes.png")

st.write(" ")
st.write(" ")
st.write(" ")

## Load dataset
df = pd.read_csv("diabetes.csv")

# page-1 Introduction
if page == "Introduction 📘":

    st.title("Diabetes Dataset Overview 🩺")

    st.markdown("##### Data Preview")
    rows = st.slider("Select number of rows",5,20,5)
    st.dataframe(df.head(rows))

    st.markdown("##### Missing Values")
    missing = df.isnull().sum()
    st.write(missing)

    if missing.sum() == 0:
        st.success("No missing values found")
    else:
        st.warning("Dataset contains missing values")

    st.markdown("##### Summary Statistics")
    if st.button("Show Describe Table"):
        st.dataframe(df.describe())

# page-2 Visualisation
elif page == "Visualization 📊":

    st.title("Data Visualization 📊")

    col_x = st.selectbox("Select X-axis variable",df.columns,index=0)
    col_y = st.selectbox("Select Y-axis variable",df.columns,index=1)

    tab1, tab2, tab3 = st.tabs(["Bar Chart 📊","Line Chart 📈","Correlation Heatmap 🔥"])

    with tab1:
        st.subheader("Bar Chart")
        st.bar_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)

    with tab2:
        st.subheader("Line Chart")
        st.line_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)

    with tab3:
        st.subheader("Correlation Matrix")
        df_numeric = df.select_dtypes(include=np.number)

        fig_corr, ax_corr = plt.subplots(figsize=(10,8))
        sns.heatmap(df_numeric.corr(),annot=True,fmt=".2f",cmap='coolwarm')
        st.pyplot(fig_corr)

