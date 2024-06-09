import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Top TF-IDF Words",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Top TF-IDF Words")

tfidf_df = pd.read_csv('tfidf_results.csv')

data = {
    "Word": tfidf_df["word"],
    "TF-IDF": tfidf_df["tfidf"]
}

custom_df = pd.DataFrame(data)

st.dataframe(custom_df)