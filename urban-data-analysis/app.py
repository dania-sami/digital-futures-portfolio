import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Urban Data Analyzer", layout="wide")

st.title("Urban Data Analytics Platform")

st.write("Upload a dataset to analyze trends in urban systems such as housing, pricing, or demand.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_columns:
        column = st.selectbox("Select column to visualize", numeric_columns)

        st.subheader("Histogram")
        fig, ax = plt.subplots()
        ax.hist(df[column].dropna(), bins=20)
        st.pyplot(fig)

        st.subheader("Insights")
        st.write(f"The distribution of {column} shows variation across the dataset.")
        st.write("This can be useful for identifying trends and patterns in urban systems.")

else:
    st.info("Please upload a CSV file to begin analysis.")
