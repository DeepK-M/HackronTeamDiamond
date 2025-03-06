# Smart Dynamic Pricing System - Backend

## Overview
The Smart Dynamic Pricing System backend is built with FastAPI and Python, serving as the engine that powers our dynamic pricing predictions and real-time data processing. It handles data integration, machine learning-based pricing recommendations, and database management with Supabase.

## Features
- **RESTful API Endpoints:**  
  Provides endpoints for fetching pricing predictions, competitor data, stock levels, and more.
- **Real-Time Data Processing:**  
  Integrates and processes real-time data from external sources.
- **Machine Learning Integration:**  
  Connects with the ML module (using Pandas and NumPy) to generate AI-based pricing recommendations.
- **Database Management:**  
  Manages product and pricing data using Supabase.
- **Interactive Documentation:**  
  Automatically generated API docs with Swagger UI (accessible at `/docs`).

## Tech Stack
- **Backend Framework:** FastAPI
- **Programming Language:** Python 3.x
- **Database:** Supabase
- **Machine Learning Libraries:** Pandas, NumPy
- **API Documentation:** Swagger UI (provided by FastAPI)
