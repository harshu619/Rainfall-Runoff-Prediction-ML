# 🌧️ Rainfall–Runoff Prediction Using Machine Learning

## 📌 Project Overview

Rainfall–runoff modelling is an important problem in hydrology and water resource engineering. This project develops a machine learning-based system to predict surface runoff response of a catchment using rainfall, climatic conditions, and catchment characteristics.

The project focuses on the Dhanbad catchment and combines traditional hydrological concepts with machine learning techniques to estimate runoff and analyze the factors influencing runoff generation.

The developed model uses environmental and hydrological parameters such as rainfall, temperature, land use changes, impervious area, and SCS Curve Number to improve runoff prediction accuracy.

---

# 🎯 Objectives

- Analyze rainfall and runoff patterns of the Dhanbad catchment
- Study the relationship between rainfall and surface runoff
- Develop predictive models for runoff estimation
- Compare machine learning predictions with conventional hydrological methods
- Identify the major parameters affecting runoff generation

---

# 📊 Dataset Description

The dataset consists of hydrological and catchment-related parameters.

## Input Features

- Annual Rainfall (mm)
- Average Temperature (°C)
- Land Use Change (%)
- Impervious Area (%)
- SCS Curve Number

## Target Variable

- Runoff (mm)

The dataset is structured for rainfall–runoff modelling and machine learning analysis.

---

# 🏗️ Methodology

The project workflow includes:

1. Data collection and preprocessing  
2. Rainfall and runoff trend analysis  
3. Correlation analysis between rainfall and runoff  
4. Machine learning model development  
5. Model performance evaluation  
6. Comparison with hydrological runoff estimation methods  

---

# 🤖 Machine Learning Models Used

## 1. Linear Regression

A statistical regression model used to understand the relationship between rainfall and runoff.

## 2. Random Forest Regression

An ensemble machine learning algorithm used to predict runoff by considering multiple hydrological and catchment parameters.

Random Forest was used because it can capture complex relationships between environmental factors and runoff response.

---

# 💧 Hydrological Model

## SCS Curve Number Method

The Soil Conservation Service Curve Number (SCS-CN) method is implemented to estimate direct runoff based on rainfall and catchment characteristics.

The machine learning predictions are compared with the traditional SCS runoff estimation approach.

---

# 📈 Analysis Performed

✔ Annual rainfall trend analysis  
✔ Runoff trend analysis  
✔ Rainfall–runoff correlation study  
✔ Linear regression modelling  
✔ Random Forest runoff prediction  
✔ Actual vs predicted runoff analysis  
✔ Feature importance evaluation  
✔ ML prediction vs SCS-CN comparison  

---

# 📏 Model Evaluation Metrics

The models are evaluated using:

## R² Score

Measures how effectively the model explains variations in runoff.

## Mean Absolute Error (MAE)

Measures the average difference between predicted and actual runoff values.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Excel Dataset Processing

---

# 🚀 Future Improvements

- Integration of real-time IMD rainfall data
- Use of satellite-based land use datasets
- GIS-based runoff mapping
- Expansion using monthly and daily rainfall records
- Deep learning models for advanced prediction

---

# 👩‍💻 Authors

### Sri Divya Harshini Nittala  
Civil Engineering Student

### Akshaya Reddy Ranabothu  
Civil Engineering Student

---

# 📌 Conclusion

This project demonstrates the application of machine learning in hydrological modelling by combining environmental data analysis with traditional runoff estimation techniques.

The developed system provides a data-driven approach for understanding rainfall–runoff behaviour and can support improved water resource planning and catchment analysis.

