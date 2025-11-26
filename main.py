from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import defaultdict
import httpx
from dotenv import load_dotenv
import os


load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


class DaySummary(BaseModel):
    date: str
    temp_min: float
    temp_max: float
    temp_avg: float
    humidity_avg: float
    wind_avg: float
    pressure_avg: float
    cloud_avg: float
    rain_total: float
    pop_avg: float


app = FastAPI(title="Weather Day-to-Day Analysis API")


@app.get("/daily-analysis", response_model=list[DaySummary])
async def daily_analysis(city: str):
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}

    async with httpx.AsyncClient() as client:
        resp = await client.get(BASE_URL, params=params)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()
    if "list" not in data:
        raise HTTPException(status_code=500, detail="Unexpected API response")

    groups = defaultdict(list)
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        groups[date].append(item)

    summaries: list[DaySummary] = []
    for date, items in groups.items():
        temps = [i["main"]["temp"] for i in items]
        hums = [i["main"]["humidity"] for i in items]
        winds = [i["wind"]["speed"] for i in items]
        pressures = [i["main"]["pressure"] for i in items]
        clouds = [i.get("clouds", {}).get("all", 0.0) for i in items]
        pops = [i.get("pop", 0.0) for i in items]

        rain_total = 0.0
        for i in items:
            rain_total += i.get("rain", {}).get("3h", 0.0)

        summaries.append(DaySummary(
            date=date,
            temp_min=min(temps),
            temp_max=max(temps),
            temp_avg=sum(temps) / len(temps),
            humidity_avg=sum(hums) / len(hums),
            wind_avg=sum(winds) / len(winds),
            pressure_avg=sum(pressures) / len(pressures),
            cloud_avg=sum(clouds) / len(clouds),
            rain_total=rain_total,
            pop_avg=sum(pops) / len(pops)
        ))

    summaries = sorted(summaries, key=lambda x: x.date)
    return summaries
