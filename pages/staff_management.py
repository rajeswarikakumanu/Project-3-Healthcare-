import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Staff Management",
    page_icon="👩‍⚕️",
    layout="wide"
)

st.title("👩‍⚕️ Staff Scheduling & Management")

# ==================================
# Create CSV if not exists
# ==================================

if not os.path.exists("data/staff_schedule.csv"):

    staff_df = pd.DataFrame(columns=[
        "staff_id",
        "name",
        "role",
        "shift",
        "start_time",
        "end_time"
    ])

    staff_df.to_csv(
        "data/staff_schedule.csv",
        index=False
    )

# ==================================
# Load Data
# ==================================

staff_df = pd.read_csv(
    "data/staff_schedule.csv"
)

# ==================================
# Dashboard Metrics
# ==================================

st.subheader("📊 Staff Overview")

total_staff = len(staff_df)

total_doctors = len(
    staff_df[
        staff_df["role"] == "Doctor"
    ]
) if not staff_df.empty else 0

total_nurses = len(
    staff_df[
        staff_df["role"] == "Nurse"
    ]
) if not staff_df.empty else 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Staff", total_staff)

with col2:
    st.metric("Doctors", total_doctors)

with col3:
    st.metric("Nurses", total_nurses)

st.divider()

# ==================================
# Add Staff
# ==================================

st.subheader("➕ Add Staff Member")

with st.form("staff_form"):

    staff_id = st.text_input("Staff ID")

    name = st.text_input("Staff Name")

    role = st.selectbox(
        "Role",
        [
            "Doctor",
            "Nurse",
            "Technician",
            "Receptionist",
            "Admin Staff"
        ]
    )

    shift = st.selectbox(
        "Shift",
        [
            "Morning",
            "Evening",
            "Night"
        ]
    )

    start_time = st.text_input(
        "Start Time",
        value="08:00"
    )

    end_time = st.text_input(
        "End Time",
        value="16:00"
    )

    submit = st.form_submit_button(
        "Add Staff"
    )

    if submit:

        new_staff = pd.DataFrame([{
            "staff_id": staff_id,
            "name": name,
            "role": role,
            "shift": shift,
            "start_time": start_time,
            "end_time": end_time
        }])

        staff_df = pd.concat(
            [staff_df, new_staff],
            ignore_index=True
        )

        staff_df.to_csv(
            "data/staff_schedule.csv",
            index=False
        )

        st.success(
            "Staff Member Added Successfully"
        )

st.divider()

# ==================================
# View Staff
# ==================================

st.subheader("📋 Staff Records")

if not staff_df.empty:

    st.dataframe(
        staff_df,
        use_container_width=True
    )

else:
    st.info("No staff records available.")

st.divider()

# ==================================
# Update Shift
# ==================================

st.subheader("🔄 Update Staff Shift")

if not staff_df.empty:

    selected_staff = st.selectbox(
        "Select Staff ID",
        staff_df["staff_id"]
    )

    new_shift = st.selectbox(
        "Select New Shift",
        [
            "Morning",
            "Evening",
            "Night"
        ]
    )

    if st.button("Update Shift"):

        staff_df.loc[
            staff_df["staff_id"] == selected_staff,
            "shift"
        ] = new_shift

        staff_df.to_csv(
            "data/staff_schedule.csv",
            index=False
        )

        st.success(
            "Shift Updated Successfully"
        )

        st.rerun()

st.divider()

# ==================================
# Delete Staff
# ==================================

st.subheader("🗑 Delete Staff")

if not staff_df.empty:

    delete_staff = st.selectbox(
        "Select Staff ID",
        staff_df["staff_id"],
        key="delete_staff"
    )

    if st.button("Delete Staff"):

        staff_df = staff_df[
            staff_df["staff_id"] != delete_staff
        ]

        staff_df.to_csv(
            "data/staff_schedule.csv",
            index=False
        )

        st.success(
            "Staff Deleted Successfully"
        )

        st.rerun()

st.divider()

# ==================================
# Analytics
# ==================================

st.subheader("📈 Staff Analytics")

if not staff_df.empty:

    col1, col2 = st.columns(2)

    with col1:

        role_chart = px.pie(
            staff_df,
            names="role",
            title="Staff Distribution"
        )

        st.plotly_chart(
            role_chart,
            use_container_width=True
        )

    with col2:

        shift_chart = px.bar(
            staff_df["shift"]
            .value_counts()
            .reset_index(),
            x="shift",
            y="count",
            title="Shift Distribution"
        )

        st.plotly_chart(
            shift_chart,
            use_container_width=True
        )

st.divider()

# ==================================
# AI Recommendation
# ==================================

st.subheader("🤖 Staffing Recommendation")

if total_staff < 10:

    st.error(
        "Hospital is understaffed. Additional staff hiring recommended."
    )

elif total_staff < 20:

    st.warning(
        "Staffing levels are moderate. Monitor workload closely."
    )

else:

    st.success(
        "Staffing levels are sufficient."
    )