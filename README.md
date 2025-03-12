🏡 House Price Prediction - Machine Learning Project

**Overview**
This project involves building and deploying a machine learning model (e.g., Linear Regression, Decision Tree, Random Forest, XGBoost) to predict house prices using regression techniques. The project covers:

- Data Preprocessing & Feature Engineering
- Model Training & Hyperparameter Tuning  
- Deployment using FastAPI
- Testing with Postman & CURL 

---

## Project Structure
```
house_price_prediction/
│── model/                        # Trained model storage
│   ├── house_price_model.pkl      # Saved ML model
│
│── app.py                          # FastAPI application
│── requirements.txt                # Dependencies list
│── test.json                       # Sample JSON for API testing
│── README.md                       # Project documentation
```

---

## Data Preprocessing & Feature Engineering
1) **Dataset Used**
Used **California Housing Dataset** from `sklearn.datasets`.

2) **Preprocessing Steps**
-  **Loaded dataset** into Pandas DataFrame.
-  **Checked missing values** → No missing values found.
-  **Feature Scaling** → Used `StandardScaler()`.
-  **Feature Selection** → Identified highly correlated features.
-  **Train-Test Split** → (80% training, 20% testing).


3) **Model Selection & Optimization**
   Models Tested:
- **Linear Regression**
- **Decision Tree**
- **Random Forest**
- **XGBoost**  

### Best Model: **XGBoost** before hyperparametr tuning (Highest R², Lowest RMSE & MAE)

### Hyperparameter Tuning
**GridSearchCV for optimizing Random Forest.**
#### **Best Model After Hyperparameter Tuning: RandomForestRegressor

----
## Deployment Strategy & API Usage Guide
### 🔹 FastAPI Deployment
- ✅ **Framework:** FastAPI (Lightweight, fast)
- ✅ **Model Storage:** Pickle (`.pkl` file)
- ✅ **Hosting:** Runs locally on `http://127.0.0.1:8000`

 **Run FastAPI Server**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## API Testing Instructions
### Test API with Postman
- Open **Postman**  
- **POST Request** to `http://127.0.0.1:8000/predict`  
- **Body → raw → JSON**, enter:
```json
{
    "MedInc": 8.0,
    "HouseAge": 25,
    "AveRooms": 6.5,
    "AveBedrms": 1.5,
    "Population": 2000,
    "AveOccup": 3.0,
    "Latitude": 37.5,
    "Longitude": -122.0"
}
```
Click **Send** → Get price prediction.

### Test API using CURL (Windows PowerShell)
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" `
    -Method Post `
    -Headers @{"Content-Type"="application/json"} `
    -Body '{"MedInc": 8.0, "HouseAge": 25, "AveRooms": 6.5, "AveBedrms": 1.5, "Population": 2000, "AveOccup": 3.0, "Latitude": 37.5, "Longitude": -122.0}' `
    -UseBasicParsing
```


