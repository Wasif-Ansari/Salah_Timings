import streamlit as st
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame
ansar_data = pd.DataFrame(data)

# Display the DataFrame as a table
st.table(ansar_data)
