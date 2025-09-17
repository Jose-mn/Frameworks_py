# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_and_clean  # if you created utils.py

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of the CORD-19 metadata (titles, dates, journals)")

@st.cache_data
def load_data():
    # loads and returns cleaned data
    return load_and_clean('metadata.csv')

df = load_data()

# Sidebar filters
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider("Select year range", min_year, max_year, (2020, max_year))
journal_filter = st.sidebar.selectbox("Top journals only?", ("No", "Yes"))

# filter dataframe
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader(f"Showing papers from {year_range[0]} to {year_range[1]} (N={len(filtered):,})")

# publications over time plot
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,3))
ax.bar(year_counts.index, year_counts.values)
ax.set_title('Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
st.pyplot(fig)

# top journals
st.subheader("Top Journals")
top_journals = filtered['journal'].fillna('Unknown').value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(8,4))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
ax2.set_xlabel('Number of papers')
st.pyplot(fig2)

# show sample table
st.subheader("Sample of the data")
st.dataframe(filtered[['title','authors','journal','publish_time','abstract_word_count']].head(50))

# allow user to download filtered data
@st.cache_data
def to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = to_csv(filtered)
st.download_button(label="Download filtered CSV", data=csv, file_name='cord19_filtered.csv', mime='text/csv')
