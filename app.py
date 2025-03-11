from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()
# Load the trained model
with open("model/housing_price_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Welcome to House Price Prediction API"}

@app.post("/predict")
def predict(features: dict):
    try:
        input_data = pd.DataFrame([features])
        prediction = model.predict(input_data)
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
