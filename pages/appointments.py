import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(
    page_title="Appointments",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Appointment Scheduling System")

# -------------------------
# Create CSV Files if Missing
# -------------------------

if not os.path.exists("data/appointments.csv"):
    appointments_df = pd.DataFrame(columns=[
        "appointment_id",
        "patient_name",
        "doctor_name",
        "appointment_date",
        "time_slot",
        "status"
    ])
    appointments_df.to_csv(
        "data/appointments.csv",
        index=False
    )

if not os.path.exists("data/doctors.csv"):
    doctors_df = pd.DataFrame({
        "doctor_id": ["D001"],
        "name": ["Dr. Sharma"],
        "specialization": ["Cardiology"]
    })

    doctors_df.to_csv(
        "data/doctors.csv",
        index=False
    )

# -------------------------
# Load Data
# -------------------------

appointments_df = pd.read_csv(
    "data/appointments.csv"
)

doctors_df = pd.read_csv(
    "data/doctors.csv"
)

# -------------------------
# Dashboard Metrics
# -------------------------

st.subheader("📊 Appointment Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Appointments",
        len(appointments_df)
    )

with col2:

    approved = len(
        appointments_df[
            appointments_df["status"] == "Approved"
        ]
    ) if not appointments_df.empty else 0

    st.metric(
        "Approved",
        approved
    )

with col3:

    pending = len(
        appointments_df[
            appointments_df["status"] == "Pending"
        ]
    ) if not appointments_df.empty else 0

    st.metric(
        "Pending",
        pending
    )

st.divider()

# -------------------------
# Book Appointment
# -------------------------

st.subheader("➕ Book Appointment")

with st.form("appointment_form"):

    appointment_id = st.text_input(
        "Appointment ID"
    )

    patient_name = st.text_input(
        "Patient Name"
    )

    doctor_name = st.selectbox(
        "Select Doctor",
        doctors_df["name"].tolist()
    )

    appointment_date = st.date_input(
        "Appointment Date",
        min_value=date.today()
    )

    time_slot = st.selectbox(
        "Select Time Slot",
        [
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM",
            "02:00 PM",
            "03:00 PM",
            "04:00 PM"
        ]
    )

    status = st.selectbox(
        "Status",
        [
            "Pending",
            "Approved"
        ]
    )

    submit = st.form_submit_button(
        "Book Appointment"
    )

    if submit:

        new_row = pd.DataFrame([{
            "appointment_id": appointment_id,
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "appointment_date": appointment_date,
            "time_slot": time_slot,
            "status": status
        }])

        appointments_df = pd.concat(
            [appointments_df, new_row],
            ignore_index=True
        )

        appointments_df.to_csv(
            "data/appointments.csv",
            index=False
        )

        st.success(
            "Appointment Booked Successfully"
        )

st.divider()

# -------------------------
# View Appointments
# -------------------------

st.subheader("📋 Appointment Records")

if not appointments_df.empty:

    st.dataframe(
        appointments_df,
        use_container_width=True
    )

else:
    st.info(
        "No appointments available."
    )

st.divider()

# -------------------------
# Delete Appointment
# -------------------------

st.subheader("🗑 Delete Appointment")

if not appointments_df.empty:

    appointment_to_delete = st.selectbox(
        "Select Appointment ID",
        appointments_df["appointment_id"]
    )

    if st.button(
        "Delete Appointment"
    ):

        appointments_df = appointments_df[
            appointments_df["appointment_id"]
            != appointment_to_delete
        ]

        appointments_df.to_csv(
            "data/appointments.csv",
            index=False
        )

        st.success(
            "Appointment Deleted Successfully"
        )

        st.rerun()

st.divider()

# -------------------------
# Search Appointments
# -------------------------

st.subheader("🔍 Search Appointment")

search_name = st.text_input(
    "Enter Patient Name"
)

if search_name:

    filtered = appointments_df[
        appointments_df["patient_name"]
        .astype(str)
        .str.contains(
            search_name,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        filtered,
        use_container_width=True
    )