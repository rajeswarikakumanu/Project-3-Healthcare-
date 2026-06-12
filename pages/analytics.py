import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Healthcare Analytics Dashboard")

# =====================================
# Helper Function
# =====================================

def load_data(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

# =====================================
# Load Data
# =====================================

patients_df = load_data("data/patients.csv")
doctors_df = load_data("data/doctors.csv")
appointments_df = load_data("data/appointments.csv")
beds_df = load_data("data/bed_management.csv")
resources_df = load_data("data/resources.csv")
reports_df = load_data("data/medical_reports.csv")
staff_df = load_data("data/staff_schedule.csv")

# =====================================
# KPI SECTION
# =====================================

st.subheader("🏥 Hospital KPI Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Patients", len(patients_df))

with col2:
    st.metric("Doctors", len(doctors_df))

with col3:
    st.metric("Appointments", len(appointments_df))

with col4:
    st.metric("Staff", len(staff_df))

st.divider()

# =====================================
# PATIENT ANALYTICS
# =====================================

st.subheader("🧑 Patient Analytics")

if not patients_df.empty:

    col1, col2 = st.columns(2)

    with col1:

        if "gender" in patients_df.columns:

            gender_chart = px.pie(
                patients_df,
                names="gender",
                title="Gender Distribution"
            )

            st.plotly_chart(
                gender_chart,
                use_container_width=True
            )

    with col2:

        if "age" in patients_df.columns:

            age_chart = px.histogram(
                patients_df,
                x="age",
                nbins=10,
                title="Age Distribution"
            )

            st.plotly_chart(
                age_chart,
                use_container_width=True
            )

st.divider()

# =====================================
# DOCTOR ANALYTICS
# =====================================

st.subheader("👨‍⚕️ Doctor Analytics")

if (
    not doctors_df.empty and
    "specialization" in doctors_df.columns
):

    doctor_chart = px.bar(
        doctors_df["specialization"]
        .value_counts()
        .reset_index(),
        x="specialization",
        y="count",
        title="Doctors by Specialization"
    )

    st.plotly_chart(
        doctor_chart,
        use_container_width=True
    )

st.divider()

# =====================================
# APPOINTMENT ANALYTICS
# =====================================

st.subheader("📅 Appointment Analytics")

if (
    not appointments_df.empty and
    "status" in appointments_df.columns
):

    appointment_chart = px.pie(
        appointments_df,
        names="status",
        title="Appointment Status"
    )

    st.plotly_chart(
        appointment_chart,
        use_container_width=True
    )

st.divider()

# =====================================
# BED ANALYTICS
# =====================================

st.subheader("🛏 Bed Occupancy Analytics")

if (
    not beds_df.empty and
    "status" in beds_df.columns
):

    bed_chart = px.pie(
        beds_df,
        names="status",
        title="Bed Occupancy"
    )

    st.plotly_chart(
        bed_chart,
        use_container_width=True
    )

st.divider()

# =====================================
# RESOURCE ANALYTICS
# =====================================

st.subheader("🏥 Resource Utilization")

if (
    not resources_df.empty and
    "resource_name" in resources_df.columns and
    "available_units" in resources_df.columns
):

    resource_chart = px.bar(
        resources_df,
        x="resource_name",
        y="available_units",
        title="Available Resources"
    )

    st.plotly_chart(
        resource_chart,
        use_container_width=True
    )

st.divider()

# =====================================
# MEDICAL REPORT ANALYTICS
# =====================================

st.subheader("🧪 Medical Risk Analysis")

if (
    not reports_df.empty and
    "risk_level" in reports_df.columns
):

    risk_chart = px.pie(
        reports_df,
        names="risk_level",
        title="Risk Distribution"
    )

    st.plotly_chart(
        risk_chart,
        use_container_width=True
    )

st.divider()

# =====================================
# STAFF ANALYTICS
# =====================================

st.subheader("👩‍⚕️ Staff Analytics")

if (
    not staff_df.empty and
    "role" in staff_df.columns
):

    staff_chart = px.bar(
        staff_df["role"]
        .value_counts()
        .reset_index(),
        x="role",
        y="count",
        title="Staff Distribution"
    )

    st.plotly_chart(
        staff_chart,
        use_container_width=True
    )

st.divider()

# =====================================
# HOSPITAL SUMMARY TABLE
# =====================================

st.subheader("📋 Hospital Summary")

summary_df = pd.DataFrame({
    "Category": [
        "Patients",
        "Doctors",
        "Appointments",
        "Beds",
        "Resources",
        "Staff"
    ],
    "Count": [
        len(patients_df),
        len(doctors_df),
        len(appointments_df),
        len(beds_df),
        len(resources_df),
        len(staff_df)
    ]
})

st.dataframe(
    summary_df,
    use_container_width=True
)

st.divider()

# =====================================
# AI INSIGHTS
# =====================================

st.subheader("🤖 AI Insights")

if len(patients_df) > 100:
    st.success(
        "High patient volume detected."
    )

if not beds_df.empty:

    occupied = len(
        beds_df[
            beds_df["status"] == "Occupied"
        ]
    )

    total = len(beds_df)

    if total > 0:

        occupancy_rate = (
            occupied / total
        ) * 100

        st.info(
            f"Current Bed Occupancy Rate: {occupancy_rate:.2f}%"
        )

        if occupancy_rate > 80:
            st.warning(
                "High bed occupancy detected. Additional beds may be required."
            )

if (
    not reports_df.empty and
    "risk_level" in reports_df.columns
):

    high_risk = len(
        reports_df[
            reports_df["risk_level"] == "High"
        ]
    )

    if high_risk > 0:

        st.error(
            f"{high_risk} high-risk patients require immediate attention."
        )

st.divider()

st.success(
    "Healthcare Analytics Dashboard Loaded Successfully ✅"
)