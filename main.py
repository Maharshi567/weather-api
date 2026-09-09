from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Weather API is running"}

@app.get("/Rajkot")
def rajkotTemperature():
    return {"Temperature": "Temperature is 28 degrees"}