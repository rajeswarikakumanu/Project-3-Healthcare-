import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Patient Outcome Prediction",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Patient Outcome Prediction System")

st.markdown(
    "Predict patient recovery chances, ICU requirement, and hospitalization duration."
)

st.divider()

# ===================================
# Patient Inputs
# ===================================

st.subheader("📝 Enter Patient Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=40
    )

    disease = st.selectbox(
        "Disease",
        [
            "Healthy",
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Hypertension",
            "Asthma"
        ]
    )

    severity = st.selectbox(
        "Severity Level",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

with col2:

    oxygen_level = st.slider(
        "Oxygen Level (%)",
        50,
        100,
        98
    )

    blood_pressure = st.slider(
        "Blood Pressure",
        80,
        220,
        120
    )

    heart_rate = st.slider(
        "Heart Rate",
        40,
        180,
        75
    )

# ===================================
# Prediction Button
# ===================================

if st.button("🔍 Predict Outcome"):

    recovery_probability = 95
    icu_required = "No"
    readmission_risk = "Low"
    mortality_risk = "Low"
    stay_days = 2

    # Severity Logic

    if severity == "Medium":
        recovery_probability = 80
        stay_days = 5
        readmission_risk = "Medium"

    if severity == "High":
        recovery_probability = 55
        stay_days = 10
        readmission_risk = "High"

    # Oxygen Logic

    if oxygen_level < 90:
        icu_required = "Yes"
        recovery_probability -= 15
        mortality_risk = "Medium"

    if oxygen_level < 80:
        icu_required = "Yes"
        recovery_probability -= 20
        mortality_risk = "High"

    # Age Logic

    if age > 65:
        recovery_probability -= 10
        stay_days += 3

    # Disease Logic

    if disease in [
        "Heart Disease",
        "Kidney Disease"
    ]:
        recovery_probability -= 10
        stay_days += 2

    recovery_probability = max(
        recovery_probability,
        5
    )

    # ==========================
    # Results
    # ==========================

    st.success("Prediction Completed Successfully")

    st.subheader("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Recovery Probability",
            f"{recovery_probability}%"
        )

    with col2:
        st.metric(
            "ICU Required",
            icu_required
        )

    with col3:
        st.metric(
            "Hospital Stay",
            f"{stay_days} Days"
        )

    st.divider()

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "Readmission Risk",
            readmission_risk
        )

    with col5:
        st.metric(
            "Mortality Risk",
            mortality_risk
        )

    # ==========================
    # Recovery Chart
    # ==========================

    chart_df = pd.DataFrame({
        "Category": [
            "Recovery",
            "Remaining Risk"
        ],
        "Value": [
            recovery_probability,
            100 - recovery_probability
        ]
    })

    fig = px.pie(
        chart_df,
        names="Category",
        values="Value",
        title="Recovery Probability Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================
    # Recommendation
    # ==========================

    st.subheader("💡 Clinical Recommendation")

    if recovery_probability >= 85:
        st.success(
            "Patient is likely to recover quickly with standard treatment."
        )

    elif recovery_probability >= 60:
        st.warning(
            "Close monitoring is recommended."
        )

    else:
        st.error(
            "Patient requires intensive monitoring and specialist care."
        )

st.divider()

# ===================================
# Information Section
# ===================================

st.subheader("📚 Outcome Metrics Explained")

info_df = pd.DataFrame({
    "Metric": [
        "Recovery Probability",
        "ICU Requirement",
        "Readmission Risk",
        "Mortality Risk",
        "Hospital Stay"
    ],
    "Description": [
        "Chance of successful recovery",
        "Whether ICU care may be needed",
        "Chance of returning after discharge",
        "Risk level of severe outcome",
        "Estimated duration of hospitalization"
    ]
})

st.dataframe(
    info_df,
    use_container_width=True
)