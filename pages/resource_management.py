import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Resource Management",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Resource Allocation & Management System")

# ==================================
# Create CSV if not exists
# ==================================

if not os.path.exists("data/resources.csv"):

    resources_df = pd.DataFrame(columns=[
        "resource_id",
        "resource_name",
        "total_units",
        "available_units",
        "status"
    ])

    resources_df.to_csv(
        "data/resources.csv",
        index=False
    )

# ==================================
# Load Data
# ==================================

resources_df = pd.read_csv(
    "data/resources.csv"
)

# ==================================
# Dashboard Metrics
# ==================================

st.subheader("📊 Resource Overview")

total_resources = len(resources_df)

total_units = (
    resources_df["total_units"].sum()
    if not resources_df.empty
    else 0
)

available_units = (
    resources_df["available_units"].sum()
    if not resources_df.empty
    else 0
)

utilized_units = total_units - available_units

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Resources", total_resources)

with col2:
    st.metric("Total Units", total_units)

with col3:
    st.metric("Available Units", available_units)

with col4:
    st.metric("Utilized Units", utilized_units)

st.divider()

# ==================================
# Add Resource
# ==================================

st.subheader("➕ Add Resource")

with st.form("resource_form"):

    resource_id = st.text_input(
        "Resource ID"
    )

    resource_name = st.selectbox(
        "Resource Name",
        [
            "Beds",
            "Ventilators",
            "Oxygen Units",
            "ECG Machine",
            "MRI Machine",
            "CT Scanner",
            "Wheelchair"
        ]
    )

    total_units_input = st.number_input(
        "Total Units",
        min_value=1,
        value=10
    )

    available_units_input = st.number_input(
        "Available Units",
        min_value=0,
        value=5
    )

    status = st.selectbox(
        "Status",
        [
            "Available",
            "Limited",
            "Critical"
        ]
    )

    submit = st.form_submit_button(
        "Add Resource"
    )

    if submit:

        new_resource = pd.DataFrame([{
            "resource_id": resource_id,
            "resource_name": resource_name,
            "total_units": total_units_input,
            "available_units": available_units_input,
            "status": status
        }])

        resources_df = pd.concat(
            [resources_df, new_resource],
            ignore_index=True
        )

        resources_df.to_csv(
            "data/resources.csv",
            index=False
        )

        st.success(
            "Resource Added Successfully"
        )

st.divider()

# ==================================
# View Resources
# ==================================

st.subheader("📋 Resource Records")

if not resources_df.empty:

    st.dataframe(
        resources_df,
        use_container_width=True
    )

else:
    st.info(
        "No resources available."
    )

st.divider()

# ==================================
# Update Resource Availability
# ==================================

st.subheader("🔄 Update Resource Availability")

if not resources_df.empty:

    selected_resource = st.selectbox(
        "Select Resource",
        resources_df["resource_id"]
    )

    updated_units = st.number_input(
        "New Available Units",
        min_value=0,
        value=0
    )

    if st.button("Update Resource"):

        resources_df.loc[
            resources_df["resource_id"] == selected_resource,
            "available_units"
        ] = updated_units

        resources_df.to_csv(
            "data/resources.csv",
            index=False
        )

        st.success(
            "Resource Updated Successfully"
        )

        st.rerun()

st.divider()

# ==================================
# Delete Resource
# ==================================

st.subheader("🗑 Delete Resource")

if not resources_df.empty:

    delete_resource = st.selectbox(
        "Select Resource ID",
        resources_df["resource_id"],
        key="delete_resource"
    )

    if st.button(
        "Delete Resource"
    ):

        resources_df = resources_df[
            resources_df["resource_id"]
            != delete_resource
        ]

        resources_df.to_csv(
            "data/resources.csv",
            index=False
        )

        st.success(
            "Resource Deleted Successfully"
        )

        st.rerun()

st.divider()

# ==================================
# Analytics
# ==================================

st.subheader("📈 Resource Analytics")

if not resources_df.empty:

    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.bar(
            resources_df,
            x="resource_name",
            y="available_units",
            title="Available Units"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with col2:

        fig2 = px.pie(
            resources_df,
            names="status",
            title="Resource Status Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

st.divider()

# ==================================
# Resource Forecasting Alert
# ==================================

st.subheader("🤖 Demand Forecasting")

if available_units < (total_units * 0.2):

    st.error(
        "⚠ Critical Resource Shortage Predicted. Immediate replenishment required."
    )

elif available_units < (total_units * 0.5):

    st.warning(
        "⚠ Resource availability is decreasing. Consider procurement."
    )

else:

    st.success(
        "✅ Resource availability is healthy."
    )

# ==================================
# Utilization Table
# ==================================

if not resources_df.empty:

    resources_df["utilization_%"] = (
        (
            resources_df["total_units"]
            - resources_df["available_units"]
        )
        / resources_df["total_units"]
    ) * 100

    st.subheader("📊 Utilization Report")

    st.dataframe(
        resources_df,
        use_container_width=True
    )