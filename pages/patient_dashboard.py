import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="Patient Dashboard", page_icon="🧑")

st.title("🧑 Patient Dashboard")

# Create CSV if not exists
if not os.path.exists("data/patients.csv"):
    df = pd.DataFrame(columns=[
        "patient_id",
        "name",
        "age",
        "gender",
        "weight",
        "height",
        "blood_group",
        "medical_history"
    ])
    df.to_csv("data/patients.csv", index=False)

# Load Data
patients = pd.read_csv("data/patients.csv")

# ==========================
# Dashboard Metrics
# ==========================
st.subheader("📊 Patient Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Patients", len(patients))

with col2:
    male_count = len(
        patients[patients["gender"] == "Male"]
    ) if not patients.empty else 0
    st.metric("Male Patients", male_count)

with col3:
    female_count = len(
        patients[patients["gender"] == "Female"]
    ) if not patients.empty else 0
    st.metric("Female Patients", female_count)

st.divider()

# ==========================
# Add Patient
# ==========================
st.subheader("➕ Add New Patient")

with st.form("patient_form"):

    patient_id = st.text_input("Patient ID")
    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0
    )

    height = st.number_input(
        "Height (cm)",
        min_value=1.0
    )

    blood_group = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    medical_history = st.text_area(
        "Medical History"
    )

    submit = st.form_submit_button(
        "Save Patient"
    )

    if submit:

        new_patient = pd.DataFrame([{
            "patient_id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "weight": weight,
            "height": height,
            "blood_group": blood_group,
            "medical_history": medical_history
        }])

        patients = pd.concat(
            [patients, new_patient],
            ignore_index=True
        )

        patients.to_csv(
            "data/patients.csv",
            index=False
        )

        st.success("Patient Added Successfully")

st.divider()

# ==========================
# View Patients
# ==========================
st.subheader("📋 Patient Records")

if not patients.empty:
    st.dataframe(
        patients,
        use_container_width=True
    )
else:
    st.info("No patient records found.")

st.divider()

# ==========================
# Delete Patient
# ==========================
st.subheader("🗑 Delete Patient")

if not patients.empty:

    patient_to_delete = st.selectbox(
        "Select Patient ID",
        patients["patient_id"]
    )

    if st.button("Delete Patient"):

        patients = patients[
            patients["patient_id"] != patient_to_delete
        ]

        patients.to_csv(
            "data/patients.csv",
            index=False
        )

        st.success("Patient Deleted Successfully")
        st.rerun()

st.divider()

# ==========================
# Charts
# ==========================
st.subheader("📈 Patient Analytics")

if not patients.empty:

    gender_chart = px.pie(
        patients,
        names="gender",
        title="Gender Distribution"
    )

    st.plotly_chart(
        gender_chart,
        use_container_width=True
    )

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
    st.subheader("📋 My Appointments")

if os.path.exists("data/appointments.csv"):

    appointments = pd.read_csv(
        "data/appointments.csv"
    )

    patient_name = st.text_input(
        "Enter Patient Name",
        key="appointment_status"
    )

    if patient_name:

        my_appointments = appointments[
            appointments["patient_name"]
            .str.lower()
            ==
            patient_name.lower()
        ]

        st.dataframe(
            my_appointments,
            use_container_width=True
        )
        # ==================================
# Available Doctors
# ==================================

st.divider()

st.subheader("👨‍⚕️ Available Doctors")

if os.path.exists("data/doctors.csv"):

    doctors_df = pd.read_csv("data/doctors.csv")

    if not doctors_df.empty:

        for _, doctor in doctors_df.iterrows():

            st.info(
                f"""
                👨‍⚕️ Doctor: {doctor['name']}
                
                🏥 Specialization: {doctor['specialization']}
                
                ⭐ Experience: {doctor['experience']}
                
                🕒 Availability: {doctor['availability']}
                """
            )

    else:
        st.info("No doctors available.")

st.subheader("🔔 Notifications")

if os.path.exists("data/notifications.csv"):

    notifications = pd.read_csv(
        "data/notifications.csv"
    )

    patient_name = st.text_input(
        "Enter Patient Name",
        key="notification_patient"
    )

    if patient_name:

        user_notifications = notifications[
            notifications["user"]
            .str.lower()
            ==
            patient_name.lower()
        ]

        st.dataframe(
            user_notifications,
            use_container_width=True
        )
