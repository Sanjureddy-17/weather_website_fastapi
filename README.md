# Weather Analysis App (FastAPI + Streamlit)

A simple weather analysis application that provides **day-to-day insights** for any city using the OpenWeather 5-day forecast API.  
The backend is built with **FastAPI**, and the frontend dashboard uses **Streamlit**.
---
## Features
### 🔹 Backend (FastAPI)
- Endpoint: `/daily-analysis?city=CityName`
- Aggregates 3-hour weather data into **daily summaries**
- Returns:
  - Minimum temperature
  - Maximum temperature
  - Average temperature  
  - Average humidity  
  - Average wind speed  
  - Average pressure  
  - Total rainfall  
  - Probability of precipitation (POP)
### 🔹 Frontend (Streamlit)
- Choose a city (e.g., Hyderabad, London, etc.)
- Select which attributes you want to visualize:
  - Temperature  
  - Humidity  
  - Wind speed  
  - Pressure  
  - Rainfall  
- Displays:
  - Raw daily weather table  
  - Line charts for selected attributes  
---
## Tech Stack
| Component | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| HTTP Client | Requests |
| Data Processing | Pandas |
| Weather Data | OpenWeatherMap API |
| Deployment (Optional) | Render / Azure / Railway |
---
## Project Structure
 WeatherWebsite/
- app.py # Streamlit frontend
- main.py # FastAPI backend
- requirements.txt
- .env # contains your API key (ignored in git)
- .gitignore
- .venv/ # virtual environment (ignored)

---

## Environment Variables

Create a `.env` file in the project root:
**OPENWEATHER_API_KEY=your_api_key_here**

**Never commit your real API key.**  

Ensure `.env` is listed in `.gitignore`.

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/weather_website_fastapi.git
cd weather_website_fastapi
```
### 2. Create Virtual Environment

```bash
python -m venv .venv
```
Activate it:

Windows:
```bash
.venv\Scripts\activate
```
Mac/Linux:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start FastAPI Backend
```bash
uvicorn main:app --reload

# Backend runs here:
http://127.0.0.1:8000/docs
```

### 5. Start Streamlit Frontend
```bash
streamlit run app.py
```

## License
This project is open-source under the **MIT** License.
