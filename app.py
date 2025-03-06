import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from database import SupabaseService
from models import DiscountPredictionInput
from utils import preprocess_input, model

db = SupabaseService()

app = FastAPI(title="Price Flow")
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Smart dynamic Price"}


@app.get("/product/{product_name}")
def get_product(product_name: str):
    return db.get_product_detail(product_name)

@app.get("/categories")
def get_categories():
    return db.get_unique_categories()

@app.get("/products/{category_name}")
def get_products(category_name: str):
    return db.get_products_by_category(category_name)


# API endpoint to predict discount
@app.post("/predict_discount/")
def predict_discount(input_data: DiscountPredictionInput):
    # Convert input data to dictionary
    input_dict = input_data.dict()

    # Preprocess input
    df = preprocess_input(input_dict)

    # Make prediction
    prediction = model.predict(df)

    max_discount = float(prediction[0])
    Customer_Type = input_dict["customer_type"]

    if Customer_Type.lower() == "premium":
        discount = 0.75 * max_discount


    elif Customer_Type.lower() == "normal":
        discount = 0.45 * max_discount

    else:
        discount = 0.25 * max_discount

    return {
        'max_discount': discount,
        
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)