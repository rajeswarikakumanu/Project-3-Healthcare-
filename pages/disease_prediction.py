import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Disease Prediction System")

st.markdown(
    "Predict possible diseases based on patient health parameters."
)

st.divider()

# ==========================
# Input Section
# ==========================

st.subheader("📝 Enter Patient Details")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=22.0
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

with col2:

    glucose = st.number_input(
        "Glucose Level",
        min_value=50,
        max_value=500,
        value=100
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=500,
        value=180
    )

    symptom = st.selectbox(
        "Primary Symptom",
        [
            "None",
            "Chest Pain",
            "Frequent Urination",
            "Fatigue",
            "Shortness of Breath",
            "Dizziness"
        ]
    )

# ==========================
# Prediction Logic
# ==========================

if st.button("🔍 Predict Disease"):

    disease = "Healthy"
    risk = 10
    severity = "Low"

    # Diabetes Rules
    if glucose > 180:
        disease = "Diabetes"
        risk = 85
        severity = "High"

    # Heart Disease Rules
    elif blood_pressure > 150 and cholesterol > 220:
        disease = "Heart Disease"
        risk = 80
        severity = "High"

    # Obesity Risk
    elif bmi > 30:
        disease = "Obesity Risk"
        risk = 70
        severity = "Medium"

    # Symptom Based
    elif symptom == "Chest Pain":
        disease = "Possible Heart Condition"
        risk = 75
        severity = "Medium"

    elif symptom == "Frequent Urination":
        disease = "Possible Diabetes"
        risk = 65
        severity = "Medium"

    st.success("Prediction Completed")

    st.subheader("📋 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Predicted Disease",
            disease
        )

    with col2:
        st.metric(
            "Risk Score",
            f"{risk}%"
        )

    with col3:
        st.metric(
            "Severity",
            severity
        )

    # Risk Gauge Data
    risk_df = pd.DataFrame({
        "Category": ["Risk", "Remaining"],
        "Value": [risk, 100 - risk]
    })

    fig = px.pie(
        risk_df,
        values="Value",
        names="Category",
        title="Disease Risk Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Recommendation
    st.subheader("💡 Recommendation")

    if risk >= 80:
        st.error(
            "Immediate consultation with a specialist is recommended."
        )

    elif risk >= 60:
        st.warning(
            "Schedule a medical checkup soon."
        )

    else:
        st.success(
            "No major health risks detected."
        )

st.divider()

# ==========================
# Disease Information
# ==========================

st.subheader("📚 Supported Predictions")

disease_data = pd.DataFrame({
    "Disease": [
        "Diabetes",
        "Heart Disease",
        "Obesity Risk"
    ],
    "Parameters": [
        "Glucose",
        "Blood Pressure + Cholesterol",
        "BMI"
    ]
})

st.dataframe(
    disease_data,
    use_container_width=True
)