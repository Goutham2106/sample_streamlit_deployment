import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("📊 Streamlit Demo App")

# Text
st.write("This is a simple Streamlit app deployed on Streamlit Cloud.")

# User input
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}, welcome to Streamlit!")

# Slider
number = st.slider("Select a number", 1, 100)

st.write("Square of the number is:", number**2)

# Generate sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Show dataframe
st.subheader("Sample Data")
st.dataframe(data)

# Chart
st.subheader("Line Chart")
st.line_chart(data)