import streamlit as st
import pandas as pd
import os
NOTIFICATION_FILE = "data/notifications.csv"


def appointment_notification(
    patient_name,
    doctor_name,
    appointment_date
):

    st.success(
        f"""
        Appointment Confirmed

        Patient: {patient_name}

        Doctor: {doctor_name}

        Date: {appointment_date}
        """
    )


def medicine_reminder(
    patient_name,
    medicine
):

    st.info(
        f"""
        Reminder

        {patient_name},

        Please take your medicine:

        {medicine}
        """
    )


def emergency_alert(
    patient_name
):

    st.error(
        f"""
        Emergency Alert

        Immediate attention required for

        {patient_name}
        """
    )


def report_notification(
    patient_name
):

    st.success(
        f"""
        Lab Report Available

        Patient: {patient_name}
        """
    )
    


def add_notification(user, message):

    if os.path.exists(NOTIFICATION_FILE):

        df = pd.read_csv(NOTIFICATION_FILE)

    else:

        df = pd.DataFrame(
            columns=[
                "notification_id",
                "user",
                "message",
                "status"
            ]
        )

    notification_id = f"N{len(df)+1:03d}"

    new_notification = {
        "notification_id": notification_id,
        "user": user,
        "message": message,
        "status": "Unread"
    }

    df = pd.concat(
        [df, pd.DataFrame([new_notification])],
        ignore_index=True
    )

    df.to_csv(
        NOTIFICATION_FILE,
        index=False
    )