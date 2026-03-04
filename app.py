import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/water_potability.csv")

df.fillna(df.median(), inplace=True)

X = df.drop("Potability", axis=1)
y = df["Potability"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

import joblib

model = joblib.load("water_model.pkl")

st.title("💧 Water Potability Prediction App")

st.write("Enter water quality parameters to predict if water is safe.")

from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.write(f"Model Accuracy: {accuracy:.2f}")

ph = st.number_input("pH", value=7.0)
hardness = st.number_input("Hardness", value=200.0)
solids = st.number_input("Solids", value=10000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=300.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", value=70.0)
turbidity = st.number_input("Turbidity", value=4.0)

if st.button("Predict"):
    input_data = pd.DataFrame([[
        ph, hardness, solids, chloramines,
        sulfate, conductivity, organic_carbon,
        trihalomethanes, turbidity
    ]], columns=X.columns)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Water is Safe to Drink")
    else:
        st.error("❌ Water is NOT Safe to Drink")