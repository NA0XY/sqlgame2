import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# API endpoint
API_URL = "http://localhost:5000"

st.title("Flask + Streamlit Integration Demo")

# Fetch data from Flask API
@st.cache_data
def fetch_data():
    response = requests.get(f"{API_URL}/api/data")
    return response.json()

# Send data to Flask API for processing
def process_data(data_to_process):
    response = requests.post(
        f"{API_URL}/api/process", 
        json=data_to_process
    )
    return response.json()

# Get initial data
data = fetch_data()

# Display the raw data
st.subheader("Raw Data from Flask API")
df = pd.DataFrame({
    'labels': data['labels'],
    'values': data['values']
})
st.dataframe(df)

# Create a simple visualization
st.subheader("Visualization of API Data")
fig = px.bar(df, x='labels', y='values', title="Data from Flask API")
st.plotly_chart(fig)

# Process data button
if st.button("Process Data with Flask"):
    processed_data = process_data(data)
    
    # Display processed results
    st.subheader("Processed Data")
    processed_df = pd.DataFrame({
        'labels': processed_data['original_labels'],
        'processed_values': processed_data['processed_values']
    })
    st.dataframe(processed_df)
    
    # Visualize processed data
    fig2 = px.bar(processed_df, x='labels', y='processed_values', 
                 title="Processed Data from Flask API")
    st.plotly_chart(fig2)
