import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel(
    "Dhanbad_Hydrology_dataset.xlsx",
    sheet_name="Annual_Rainfall_Runoff"
)

# Display first 5 rows
print(df.head())

# Display column names
print(df.columns)

# Plot rainfall trend
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df.iloc[:,1], marker="o")

plt.xlabel("Year")
plt.ylabel("Annual Rainfall (mm)")
plt.title("Annual Rainfall Trend - Dhanbad Catchment")

plt.grid(True)
plt.show()
# Rainfall vs Runoff relationship

plt.figure(figsize=(8,5))

plt.scatter(
    df["Annual Rainfall (mm)"],
    df["Runoff (mm)"],
    marker="o"
)

plt.xlabel("Annual Rainfall (mm)")
plt.ylabel("Runoff (mm)")
plt.title("Rainfall - Runoff Relationship")

plt.grid(True)
plt.show()
# Correlation between rainfall and runoff

correlation = df["Annual Rainfall (mm)"].corr(
    df["Runoff (mm)"]
)

print("Rainfall-Runoff Correlation:", correlation)
# Runoff trend graph

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Runoff (mm)"],
    marker="o"
)

plt.xlabel("Year")
plt.ylabel("Runoff (mm)")
plt.title("Annual Runoff Trend - Dhanbad Catchment")

plt.grid(True)
plt.show()
# Linear Regression Model - Rainfall to Runoff Prediction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


# Selecting input and output

X = df[["Annual Rainfall (mm)"]]

y = df["Runoff (mm)"]


# Split data into training and testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)


# Create model

model = LinearRegression()


# Train model

model.fit(X_train, y_train)


# Prediction

y_pred = model.predict(X_test)


# Accuracy

r2 = r2_score(y_test, y_pred)

mae = mean_absolute_error(y_test, y_pred)


print("R² Score:", r2)

print("Mean Absolute Error:", mae)


# Predict runoff for new rainfall value

rainfall = pd.DataFrame(
    [[1600]],
    columns=["Annual Rainfall (mm)"]
)

predicted_runoff = model.predict(rainfall)

print(
    "Predicted runoff for 1600 mm rainfall:",
    predicted_runoff[0],
    "mm"
)
import matplotlib.pyplot as plt

# Plotting the original data points
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Actual Data", marker="o")

# Plotting the Linear Regression line of best fit
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line (Prediction)")

plt.xlabel("Annual Rainfall (mm)")
plt.ylabel("Runoff (mm)")
plt.title("Linear Regression Model - Dhanbad Catchment")
plt.legend()
plt.grid(True)
plt.show()
# Actual vs Predicted Runoff graph

plt.figure(figsize=(8,5))

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel("Actual Runoff (mm)")
plt.ylabel("Predicted Runoff (mm)")
plt.title("Actual vs Predicted Runoff - Linear Regression")

plt.grid(True)
plt.show()
# Read catchment parameters

catchment = pd.read_excel(
    "Dhanbad_Hydrology_dataset.xlsx",
    sheet_name="Catchment_Parameters"
)

print(catchment.head())
df_ml = pd.merge(
    df,
    catchment,
    on="Year"
)

print(df_ml.head())
# Merge rainfall-runoff data with catchment parameters

df_ml = pd.merge(
    df,
    catchment,
    on="Year"
)

print(df_ml.head())
print(df_ml.columns)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt


# Features

X = df_ml[
[
"Annual Rainfall (mm)",
"Avg Temp (°C)",
"Land Use Change (%)",
"Impervious Area (%)",
"SCS Curve Number"
]
]


# Target

y = df_ml["Runoff (mm)"]


# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Random Forest Model

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Training

model.fit(X_train, y_train)


# Prediction on test data

y_pred = model.predict(X_test)


# Model Evaluation

print("Random Forest R2 Score:", r2_score(y_test, y_pred))

print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))


# Prediction on complete dataset for more points

all_predictions = model.predict(X)


# Actual vs Predicted graph

plt.figure(figsize=(8,5))

plt.scatter(
    y,
    all_predictions,
    marker="o"
)


plt.xlabel("Actual Runoff (mm)")
plt.ylabel("Predicted Runoff (mm)")

plt.title(
"Actual vs Predicted Runoff - Random Forest (All Data)"
)


plt.grid(True)

plt.show()
# Feature Importance

importance = model.feature_importances_

features = X.columns


plt.figure(figsize=(8,5))

plt.bar(
    features,
    importance
)

plt.xlabel("Features")
plt.ylabel("Importance")

plt.title(
"Random Forest Feature Importance for Runoff Prediction"
)

plt.xticks(rotation=45)

plt.grid(True)

plt.show()


# Print values

for feature, value in zip(features, importance):
    print(feature, ":", value)
# Model Comparison

from sklearn.linear_model import LinearRegression


# Linear Regression Model

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)


# Prediction

lr_pred = lr_model.predict(X_test)


# Scores

lr_r2 = r2_score(y_test, lr_pred)

lr_mae = mean_absolute_error(y_test, lr_pred)



# Random Forest scores

rf_r2 = r2_score(y_test, y_pred)

rf_mae = mean_absolute_error(y_test, y_pred)



print("Linear Regression R2 Score:", lr_r2)

print("Linear Regression MAE:", lr_mae)


print("Random Forest R2 Score:", rf_r2)

print("Random Forest MAE:", rf_mae)



# Comparison Graph

models = [
    "Linear Regression",
    "Random Forest"
]

scores = [
    lr_r2,
    rf_r2
]


plt.figure(figsize=(7,5))

plt.bar(
    models,
    scores
)


plt.xlabel("Models")

plt.ylabel("R2 Score")

plt.title(
"Model Performance Comparison"
)

plt.grid(True)

plt.show()
# SCS Curve Number Runoff Calculation

def scs_runoff(P, CN):

    S = (25400 / CN) - 254

    if P > 0.2*S:
        Q = ((P - 0.2*S)**2) / (P + 0.8*S)
    else:
        Q = 0

    return Q


# Example prediction

rainfall = 1500
CN = 80

scs_runoff_value = scs_runoff(rainfall, CN)


print(
"SCS Curve Number Runoff:",
scs_runoff_value,
"mm"
)
# Compare ML and SCS runoff

# 1. Create a proper DataFrame with matching column names for the RF prediction
prediction_data = pd.DataFrame([{
    "Annual Rainfall (mm)": 1500,
    "Avg Temp (°C)": 27,
    "Land Use Change (%)": 10,
    "Impervious Area (%)": 28,
    "SCS Curve Number": 80
}])

# 2. Pass the DataFrame to the model instead of a raw list
ml_prediction = model.predict(prediction_data)


print(
"Random Forest Predicted Runoff:",
ml_prediction[0],
"mm"
)

print(
"SCS Calculated Runoff:",
scs_runoff_value,
"mm"
)
import pickle

# Save model

with open("runoff_prediction_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model saved successfully")
# Save final dataset

df_ml.to_csv(
    "Dhanbad_Runoff_Final_Dataset.csv",
    index=False
)

print("Dataset saved")