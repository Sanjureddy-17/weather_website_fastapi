import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/daily-analysis"


ATTR_MAP = {
    "A. Temperature (min/max/avg)": ["temp_min", "temp_max", "temp_avg"],
    "B. Humidity (avg)": ["humidity_avg"],
    "C. Wind Speed (avg)": ["wind_avg"],
    "D. Pressure (avg)": ["pressure_avg"],
    "E. Rainfall (total)": ["rain_total"],
}

st.title("Weather Day-to-Day Analysis")

city = st.text_input("City name", value="Hyderabad")


selected_sections = st.multiselect(
    "Choose attributes to display",
    list(ATTR_MAP.keys()),
    default=[
        "A. Temperature (min/max/avg)",
        "B. Humidity (avg)",
        "E. Rainfall (total)",
    ],
)

if st.button("Get Analysis"):
    if not city:
        st.error("Please enter a city.")
    else:
        with st.spinner("Fetching data..."):
            resp = requests.get(API_URL, params={"city": city})

        if resp.status_code != 200:
            st.error(f"API error: {resp.text}")
        else:
            data = resp.json()
            df = pd.DataFrame(data)
            df["date"] = pd.to_datetime(df["date"])
            df = df.set_index("date")

            st.subheader(f"Raw daily data for {city}")
            st.dataframe(df)

            for section in selected_sections:
                cols = ATTR_MAP[section]
                st.subheader(section)
                st.line_chart(df[cols])
