from typing import AsyncGenerator
import os
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
WEIGHT = 100
HEIGHT = 180
AGE = 20
TOKEN = os.environ.get("TOKEN")
SHEET_NAME = "copyOfMyWorkouts/workouts"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}





nle_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query" : input("Tell me which exercise you did: "),
    "gender" : "male",
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE
}


response = requests.post(url=nle_endpoint,json=params,headers=headers)
data = response.json()
print(data)


sheety_endpoint =  "https://api.sheety.co/1853d7fe1239dfd4c9986289b2576ade/copyOfMyWorkouts/workouts"

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout" :{
            "date" : date,
            "time" : time,
            "exercise" : exercise["user_input"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }

    }
    sheet_response = requests.post(url=sheety_endpoint,json=sheet_inputs,auth=(os.environ.get("USERNAME"),os.environ.get("PASSWORD")))
    print(sheet_response.text)
