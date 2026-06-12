import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Medical Report Analysis",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Medical Report Analysis System")

# =====================================
# Create CSV if not exists
# =====================================

if not os.path.exists("data/medical_reports.csv"):

    reports_df = pd.DataFrame(columns=[
        "patient_id",
        "patient_name",
        "report_type",
        "blood_sugar",
        "cholesterol",
        "blood_pressure",
        "risk_level"
    ])

    reports_df.to_csv(
        "data/medical_reports.csv",
        index=False
    )

# =====================================
# Load Data
# =====================================

reports_df = pd.read_csv(
    "data/medical_reports.csv"
)

# =====================================
# Upload Medical Report
# =====================================

st.subheader("📄 Add Medical Report")

with st.form("report_form"):

    patient_id = st.text_input(
        "Patient ID"
    )

    patient_name = st.text_input(
        "Patient Name"
    )

    report_type = st.selectbox(
        "Report Type",
        [
            "Blood Test",
            "ECG",
            "MRI",
            "CT Scan",
            "X-Ray"
        ]
    )

    blood_sugar = st.number_input(
        "Blood Sugar (mg/dL)",
        min_value=0,
        value=100
    )

    cholesterol = st.number_input(
        "Cholesterol (mg/dL)",
        min_value=0,
        value=180
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        value=120
    )

    submit = st.form_submit_button(
        "Analyze Report"
    )

    if submit:

        # Risk Detection Logic

        risk_level = "Low"

        if (
            blood_sugar > 180
            or cholesterol > 240
            or blood_pressure > 160
        ):
            risk_level = "High"

        elif (
            blood_sugar > 140
            or cholesterol > 200
            or blood_pressure > 140
        ):
            risk_level = "Medium"

        new_report = pd.DataFrame([{
            "patient_id": patient_id,
            "patient_name": patient_name,
            "report_type": report_type,
            "blood_sugar": blood_sugar,
            "cholesterol": cholesterol,
            "blood_pressure": blood_pressure,
            "risk_level": risk_level
        }])

        reports_df = pd.concat(
            [reports_df, new_report],
            ignore_index=True
        )

        reports_df.to_csv(
            "data/medical_reports.csv",
            index=False
        )

        st.success(
            f"Report Analyzed Successfully! Risk Level: {risk_level}"
        )

st.divider()

# =====================================
# Risk Alerts
# =====================================

st.subheader("🚨 Risk Assessment")

if not reports_df.empty:

    high_risk = reports_df[
        reports_df["risk_level"] == "High"
    ]

    medium_risk = reports_df[
        reports_df["risk_level"] == "Medium"
    ]

    st.metric(
        "High Risk Patients",
        len(high_risk)
    )

    st.metric(
        "Medium Risk Patients",
        len(medium_risk)
    )

    if len(high_risk) > 0:
        st.error(
            "⚠ High-risk patients detected. Immediate medical attention recommended."
        )

st.divider()

# =====================================
# View Reports
# =====================================

st.subheader("📋 Medical Reports")

if not reports_df.empty:

    st.dataframe(
        reports_df,
        use_container_width=True
    )

else:

    st.info(
        "No reports available."
    )

st.divider()

# =====================================
# Search Patient
# =====================================

st.subheader("🔍 Search Patient Report")

search_patient = st.text_input(
    "Enter Patient Name"
)

if search_patient:

    result = reports_df[
        reports_df["patient_name"]
        .astype(str)
        .str.contains(
            search_patient,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

st.divider()

# =====================================
# Analytics
# =====================================

st.subheader("📊 Report Analytics")

if not reports_df.empty:

    col1, col2 = st.columns(2)

    with col1:

        risk_chart = px.pie(
            reports_df,
            names="risk_level",
            title="Risk Level Distribution"
        )

        st.plotly_chart(
            risk_chart,
            use_container_width=True
        )

    with col2:

        report_chart = px.bar(
            reports_df["report_type"]
            .value_counts()
            .reset_index(),
            x="report_type",
            y="count",
            title="Report Type Distribution"
        )

        st.plotly_chart(
            report_chart,
            use_container_width=True
        )

st.divider()

# =====================================
# Abnormal Value Detection
# =====================================

st.subheader("🩺 Abnormal Value Detection")

if not reports_df.empty:

    abnormal = reports_df[
        (reports_df["blood_sugar"] > 180)
        | (reports_df["cholesterol"] > 240)
        | (reports_df["blood_pressure"] > 160)
    ]

    if not abnormal.empty:

        st.warning(
            "Abnormal reports detected."
        )

        st.dataframe(
            abnormal,
            use_container_width=True
        )

    else:

        st.success(
            "No abnormal reports found."
        )
    # =====================================
# Download Patient Report
# =====================================

st.divider()

st.subheader("⬇ Download Patient Report")

if not reports_df.empty:

    selected_patient = st.selectbox(
        "Select Patient",
        reports_df["patient_name"].unique()
    )

    patient_report = reports_df[
        reports_df["patient_name"] == selected_patient
    ]

    csv_data = patient_report.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📄 Download Report",
        data=csv_data,
        file_name=f"{selected_patient}_report.csv",
        mime="text/csv"
    )