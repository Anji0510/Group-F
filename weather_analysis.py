import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")  # Modern, aesthetic chart style
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #64b5f6, #1976d2);
        color: white;
        padding: 20px;
    }
    [data-testid="stSidebar"] .css-1d391kg {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.sidebar.title("🎯 Weather Insights")  # Sidebar title with an emoji

st.sidebar.subheader("🌦️Explore 5-day weather trends!")

st.sidebar.markdown(
    """
    - View **temperature, humidity, and wind speed** trends over the next 5 days.  
    - Interactive **line charts** show daily variations.  
    - A **scatter plot** compares **temperature vs. humidity**.  
    - Analyze weather conditions to plan your days better! ✈️😎  
    """
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #90caf9;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("📊 Weather Forecast Visualization")




# Load CSV
csv_file = "weather_forecast.csv"

if not os.path.exists(csv_file):
    st.error("No data available. Please fetch the forecast first from the main page.")
else:
    weather_df = pd.read_csv(csv_file)

    if not weather_df.empty:
        st.subheader("Forecast Data")
        st.dataframe(weather_df)

        # Temperature Trend
        st.subheader("Temperature Trend (°C)")
        st.line_chart(weather_df.set_index("Date")["Temperature"])

        # Humidity Trend
        st.subheader("Humidity Trend (%)")
        st.bar_chart(weather_df.set_index("Date")["Humidity"])

        # Wind Speed Trend
        st.subheader("Wind Speed Trend (m/s)")
        st.line_chart(weather_df.set_index("Date")["Wind Speed"])

        # Scatter Plot
        st.subheader("Scatter Plot: Temperature vs Humidity")
        fig, ax = plt.subplots()
        ax.scatter(weather_df["Temperature"], weather_df["Humidity"], color="blue", alpha=0.7)
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Humidity (%)")
        ax.set_title("Temperature vs Humidity")
        st.pyplot(fig)

    else:
        st.error("The CSV file is empty. Please fetch the forecast from the main page.")

# Sidebar Navigation
st.sidebar.markdown("---")  # Divider for better structure
if st.sidebar.button("🏠 Back to Home Page"):
    st.switch_page("weatherapp.py")  # Navigates back to main.py

