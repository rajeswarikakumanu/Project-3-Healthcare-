import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Treatment Recommendation",
    page_icon="💊",
    layout="wide"
)

st.title("💊 AI Treatment Recommendation System")

st.markdown(
    "Get treatment recommendations based on predicted disease."
)

st.divider()

# ==========================
# Disease Selection
# ==========================

st.subheader("🩺 Select Disease")

disease = st.selectbox(
    "Predicted Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Hypertension",
        "Asthma",
        "Obesity",
        "Healthy"
    ]
)

# ==========================
# Recommendation Logic
# ==========================

recommendations = {
    "Diabetes": {
        "specialist": "Endocrinologist",
        "tests": [
            "HbA1c Test",
            "Blood Glucose Test",
            "Kidney Function Test"
        ],
        "medications": [
            "Metformin",
            "Insulin (if prescribed)"
        ],
        "advice": [
            "Reduce sugar intake",
            "Exercise regularly",
            "Monitor blood glucose daily"
        ]
    },

    "Heart Disease": {
        "specialist": "Cardiologist",
        "tests": [
            "ECG",
            "Echocardiogram",
            "Lipid Profile"
        ],
        "medications": [
            "Aspirin (if prescribed)",
            "Statins"
        ],
        "advice": [
            "Low-fat diet",
            "Regular exercise",
            "Avoid smoking"
        ]
    },

    "Kidney Disease": {
        "specialist": "Nephrologist",
        "tests": [
            "Creatinine Test",
            "Urine Analysis",
            "Kidney Ultrasound"
        ],
        "medications": [
            "As prescribed by nephrologist"
        ],
        "advice": [
            "Limit salt intake",
            "Drink adequate water",
            "Regular monitoring"
        ]
    },

    "Hypertension": {
        "specialist": "General Physician",
        "tests": [
            "Blood Pressure Monitoring",
            "ECG"
        ],
        "medications": [
            "Antihypertensive drugs"
        ],
        "advice": [
            "Reduce salt intake",
            "Exercise daily",
            "Manage stress"
        ]
    },

    "Asthma": {
        "specialist": "Pulmonologist",
        "tests": [
            "Spirometry",
            "Chest X-Ray"
        ],
        "medications": [
            "Inhalers",
            "Bronchodilators"
        ],
        "advice": [
            "Avoid dust and smoke",
            "Use inhaler as directed"
        ]
    },

    "Obesity": {
        "specialist": "Dietitian",
        "tests": [
            "BMI Assessment",
            "Blood Sugar Test"
        ],
        "medications": [
            "Weight management program"
        ],
        "advice": [
            "Balanced diet",
            "Daily exercise",
            "Reduce processed foods"
        ]
    },

    "Healthy": {
        "specialist": "No specialist required",
        "tests": [
            "Annual Health Checkup"
        ],
        "medications": [
            "None"
        ],
        "advice": [
            "Maintain healthy lifestyle",
            "Regular exercise",
            "Balanced diet"
        ]
    }
}

if st.button("🔍 Generate Recommendation"):

    result = recommendations[disease]

    st.success("Recommendations Generated Successfully")

    st.subheader("👨‍⚕️ Recommended Specialist")
    st.info(result["specialist"])

    st.subheader("🧪 Recommended Tests")
    for test in result["tests"]:
        st.write(f"✅ {test}")

    st.subheader("💊 Suggested Medications")
    for med in result["medications"]:
        st.write(f"💊 {med}")

    st.subheader("📋 Lifestyle Advice")
    for advice in result["advice"]:
        st.write(f"✔️ {advice}")

    # Summary Table
    summary_df = pd.DataFrame({
        "Category": ["Specialist", "Tests", "Medications"],
        "Details": [
            result["specialist"],
            ", ".join(result["tests"]),
            ", ".join(result["medications"])
        ]
    })

    st.subheader("📊 Recommendation Summary")
    st.dataframe(
        summary_df,
        use_container_width=True
    )

st.divider()

st.subheader("ℹ️ Disclaimer")
st.warning(
    "These recommendations are for educational purposes only. "
    "Always consult a qualified healthcare professional before "
    "making medical decisions."
)