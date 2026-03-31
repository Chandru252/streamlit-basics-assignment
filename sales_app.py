import streamlit as st
import pandas as pd

# App Title
st.title("Sales Summary Dashboard")
st.subheader("Filter sales data by product category")

# Hardcoded Dataset
data = {
    "Product": ["Laptop", "Shirt", "Mobile", "Jeans", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 2000, 30000, 2500, 15000]
}

df = pd.DataFrame(data)

# Sidebar Filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

# Filter Data
filtered_df = df[df["Category"] == category]

# Display Filtered Data
st.write(f"Showing data for category: {category}")
st.dataframe(filtered_df)

# Line Chart
st.line_chart(filtered_df["Sales"])





