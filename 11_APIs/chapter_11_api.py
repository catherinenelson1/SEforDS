from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from chapter_11_functions import fit_trendline, country_trendline

app = FastAPI()


@app.get("/say_hi/")
def say_hi():
    return {"Hi": "There"}


@app.get("/say_hello/{name}")
def say_hello(name):
    return {"Hello": name}


class TrendlineInput(BaseModel):
    timestamps: List[int]
    data: List[float]


@app.post(
    "/fit_trendline/",
    summary="Fit a trendline to any data",
    description="Provide a list of integer timestamps and a list of floats",
)
def calculate_trendline(trendline_input: TrendlineInput):
    slope, r_squared = fit_trendline(trendline_input.timestamps, trendline_input.data)
    return {"slope": slope, "r_squared": r_squared}


@app.get("/country_trendline/{country}")
def calculate_country_trendline(country: str):
    slope, r_squared = country_trendline(country)
    return {"slope": slope, "r_squared": r_squared}
