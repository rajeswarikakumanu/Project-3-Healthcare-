import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Admin Dashboard")

# -------------------------
# Load Data Safely
# -------------------------

def load_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

patients = load_csv("data/patients.csv")
doctors = load_csv("data/doctors.csv")
appointments = load_csv("data/appointments.csv")
beds = load_csv("data/bed_management.csv")
resources = load_csv("data/resources.csv")

# -------------------------
# KPI Cards
# -------------------------

st.subheader("📊 Hospital Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍⚕️ Doctors",
        len(doctors)
    )

with col2:
    st.metric(
        "🧑 Patients",
        len(patients)
    )

with col3:
    st.metric(
        "📅 Appointments",
        len(appointments)
    )

with col4:
    st.metric(
        "🛏 Beds",
        len(beds)
    )

st.divider()

# -------------------------
# Patient Analytics
# -------------------------

st.subheader("🧑 Patient Analytics")

if not patients.empty and "gender" in patients.columns:

    col1, col2 = st.columns(2)

    with col1:

        gender_chart = px.pie(
            patients,
            names="gender",
            title="Gender Distribution"
        )

        st.plotly_chart(
            gender_chart,
            use_container_width=True
        )

    with col2:

        if "age" in patients.columns:

            age_chart = px.histogram(
                patients,
                x="age",
                nbins=10,
                title="Age Distribution"
            )

            st.plotly_chart(
                age_chart,
                use_container_width=True
            )

st.divider()

# -------------------------
# Doctor Analytics
# -------------------------

st.subheader("👨‍⚕️ Doctor Analytics")

if not doctors.empty and "specialization" in doctors.columns:

    specialization_chart = px.bar(
        doctors["specialization"].value_counts().reset_index(),
        x="specialization",
        y="count",
        title="Doctors by Specialization"
    )

    st.plotly_chart(
        specialization_chart,
        use_container_width=True
    )

st.divider()

# -------------------------
# Bed Management
# -------------------------

st.subheader("🛏 Bed Occupancy")

if not beds.empty and "status" in beds.columns:

    bed_chart = px.pie(
        beds,
        names="status",
        title="Bed Status"
    )

    st.plotly_chart(
        bed_chart,
        use_container_width=True
    )

st.divider()

# -------------------------
# Resource Management
# -------------------------

st.subheader("🏥 Resource Utilization")

if not resources.empty:

    if (
        "resource_name" in resources.columns and
        "available_units" in resources.columns
    ):

        resource_chart = px.bar(
            resources,
            x="resource_name",
            y="available_units",
            title="Available Resources"
        )

        st.plotly_chart(
            resource_chart,
            use_container_width=True
        )

st.divider()

# -------------------------
# Recent Data
# -------------------------

tab1, tab2, tab3 = st.tabs([
    "Patients",
    "Doctors",
    "Appointments"
])

with tab1:

    st.subheader("Recent Patients")

    if not patients.empty:
        st.dataframe(
            patients.tail(10),
            use_container_width=True
        )
    else:
        st.info("No patient data available.")

with tab2:

    st.subheader("Doctors")

    if not doctors.empty:
        st.dataframe(
            doctors,
            use_container_width=True
        )
    else:
        st.info("No doctor data available.")

with tab3:

    st.subheader("Appointments")

    if not appointments.empty:
        st.dataframe(
            appointments,
            use_container_width=True
        )
    else:
        st.info("No appointment data available.")

st.divider()

# -------------------------
# Hospital Summary
# -------------------------

st.subheader("📋 Summary")

st.success(
    f"""
    Total Patients: {len(patients)}

    Total Doctors: {len(doctors)}

    Total Appointments: {len(appointments)}

    Total Beds: {len(beds)}
    """
)