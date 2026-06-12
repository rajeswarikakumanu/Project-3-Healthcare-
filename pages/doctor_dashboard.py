import streamlit as st
import pandas as pd
import os
import plotly.express as px
from utils.notifications import add_notification

st.set_page_config(
    page_title="Doctor Dashboard",
    page_icon="👨‍⚕️",
    layout="wide"
)

st.title("👨‍⚕️ Doctor Dashboard")

# Create CSV if it doesn't exist
if not os.path.exists("data/doctors.csv"):
    doctors_df = pd.DataFrame(columns=[
        "doctor_id",
        "name",
        "specialization",
        "experience",
        "qualification",
        "availability"
    ])
    doctors_df.to_csv("data/doctors.csv", index=False)

# Load data
doctors_df = pd.read_csv("data/doctors.csv")

# ==========================
# Statistics
# ==========================
st.subheader("📊 Doctor Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Doctors", len(doctors_df))

with col2:
    available = len(
        doctors_df[
            doctors_df["availability"] == "Available"
        ]
    ) if not doctors_df.empty else 0

    st.metric("Available Doctors", available)

with col3:
    busy = len(
        doctors_df[
            doctors_df["availability"] == "Busy"
        ]
    ) if not doctors_df.empty else 0

    st.metric("Busy Doctors", busy)

st.divider()

# ==========================
# Add Doctor
# ==========================
st.subheader("➕ Add New Doctor")

with st.form("doctor_form"):

    doctor_id = st.text_input("Doctor ID")

    name = st.text_input("Doctor Name")

    specialization = st.selectbox(
        "Specialization",
        [
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Pediatrics",
            "Dermatology",
            "General Medicine",
            "Oncology"
        ]
    )

    experience = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=50,
        value=1
    )

    qualification = st.text_input(
        "Qualification"
    )

    availability = st.selectbox(
        "Availability",
        ["Available", "Busy", "On Leave"]
    )

    submit = st.form_submit_button(
        "Add Doctor"
    )

    if submit:

        new_doctor = pd.DataFrame([{
            "doctor_id": doctor_id,
            "name": name,
            "specialization": specialization,
            "experience": experience,
            "qualification": qualification,
            "availability": availability
        }])

        doctors_df = pd.concat(
            [doctors_df, new_doctor],
            ignore_index=True
        )

        doctors_df.to_csv(
            "data/doctors.csv",
            index=False
        )

        st.success("Doctor Added Successfully")

st.divider()

# ==========================
# View Doctors
# ==========================
st.subheader("📋 Doctor Records")

if not doctors_df.empty:

    st.dataframe(
        doctors_df,
        use_container_width=True
    )

else:
    st.info("No doctor records found.")

st.divider()

# ==========================
# Delete Doctor
# ==========================
st.subheader("🗑 Delete Doctor")

if not doctors_df.empty:

    doctor_to_delete = st.selectbox(
        "Select Doctor ID",
        doctors_df["doctor_id"]
    )

    if st.button("Delete Doctor"):

        doctors_df = doctors_df[
            doctors_df["doctor_id"] != doctor_to_delete
        ]

        doctors_df.to_csv(
            "data/doctors.csv",
            index=False
        )

        st.success("Doctor Deleted Successfully")
        st.rerun()

st.divider()

# ==========================
# Analytics
# ==========================
st.subheader("📈 Doctor Analytics")

if not doctors_df.empty:

    spec_chart = px.pie(
        doctors_df,
        names="specialization",
        title="Doctor Specialization Distribution"
    )

    st.plotly_chart(
        spec_chart,
        use_container_width=True
    )

    exp_chart = px.histogram(
        doctors_df,
        x="experience",
        nbins=10,
        title="Experience Distribution"
    )

    st.plotly_chart(
        exp_chart,
        use_container_width=True
    )
    st.subheader("📅 Appointment Requests")

appointments = pd.read_csv("data/appointments.csv")

if not appointments.empty:

    st.dataframe(appointments)

    selected_id = st.selectbox(
        "Select Appointment ID",
        appointments["appointment_id"]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("✅ Approve"):

            appointments.loc[
                appointments["appointment_id"] == selected_id,
                "status"
            ] = "Approved"
            patient_name=appointments.loc[
                appointments["appointment_id"] == selected_id,
                "patient_name"
            ].iloc[0]
            add_notification(patient_name,
                              "Your appointment has been approved by the doctor.")
            

            appointments.to_csv(
                "data/appointments.csv",
                index=False
            )

            st.success(
                "Appointment Approved"
            )

            st.rerun()

    with col2:

        if st.button("❌ Reject"):

            appointments.loc[
                appointments["appointment_id"] == selected_id,
                "status"
            ] = "Rejected"
            patient_name=appointments.loc[
                appointments["appointment_id"] == selected_id,
                "patient_name"
            ].iloc[0]
            add_notification(patient_name,
                              "Your appointment has been rejected by the doctor.")
            

            appointments.to_csv(
                "data/appointments.csv",
                index=False
            )

            st.success(
                "Appointment Rejected"
            )

            st.rerun()
            st.subheader("🧑 Registered Patients")

if os.path.exists("data/patients.csv"):

    patients = pd.read_csv(
        "data/patients.csv"
    )

    st.dataframe(
        patients,
        use_container_width=True
    )