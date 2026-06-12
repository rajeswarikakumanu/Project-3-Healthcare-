import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Bed Management",
    page_icon="🛏",
    layout="wide"
)

st.title("🛏 Bed Management System")

# ==================================
# Create CSV if not exists
# ==================================

if not os.path.exists("data/bed_management.csv"):
    
    bed_df = pd.DataFrame(columns=[
        "bed_id",
        "ward",
        "bed_type",
        "status"
    ])

    bed_df.to_csv(
        "data/bed_management.csv",
        index=False
    )

# ==================================
# Load Data
# ==================================

bed_df = pd.read_csv(
    "data/bed_management.csv"
)

# ==================================
# Metrics
# ==================================

st.subheader("📊 Bed Overview")

total_beds = len(bed_df)

available_beds = len(
    bed_df[
        bed_df["status"] == "Available"
    ]
) if not bed_df.empty else 0

occupied_beds = len(
    bed_df[
        bed_df["status"] == "Occupied"
    ]
) if not bed_df.empty else 0

icu_beds = len(
    bed_df[
        bed_df["bed_type"] == "ICU"
    ]
) if not bed_df.empty else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Beds", total_beds)

with col2:
    st.metric("Available Beds", available_beds)

with col3:
    st.metric("Occupied Beds", occupied_beds)

with col4:
    st.metric("ICU Beds", icu_beds)

st.divider()

# ==================================
# Add Bed
# ==================================

st.subheader("➕ Add New Bed")

with st.form("bed_form"):

    bed_id = st.text_input(
        "Bed ID"
    )

    ward = st.selectbox(
        "Ward",
        [
            "General",
            "ICU",
            "Emergency",
            "Pediatrics"
        ]
    )

    bed_type = st.selectbox(
        "Bed Type",
        [
            "Normal",
            "ICU",
            "Emergency"
        ]
    )

    status = st.selectbox(
        "Status",
        [
            "Available",
            "Occupied"
        ]
    )

    submit = st.form_submit_button(
        "Add Bed"
    )

    if submit:

        new_bed = pd.DataFrame([{
            "bed_id": bed_id,
            "ward": ward,
            "bed_type": bed_type,
            "status": status
        }])

        bed_df = pd.concat(
            [bed_df, new_bed],
            ignore_index=True
        )

        bed_df.to_csv(
            "data/bed_management.csv",
            index=False
        )

        st.success(
            "Bed Added Successfully"
        )

st.divider()

# ==================================
# View Beds
# ==================================

st.subheader("📋 Bed Records")

if not bed_df.empty:

    st.dataframe(
        bed_df,
        use_container_width=True
    )

else:
    st.info(
        "No bed records available."
    )

st.divider()

# ==================================
# Update Bed Status
# ==================================

st.subheader("🔄 Update Bed Status")

if not bed_df.empty:

    selected_bed = st.selectbox(
        "Select Bed",
        bed_df["bed_id"]
    )

    new_status = st.selectbox(
        "New Status",
        [
            "Available",
            "Occupied"
        ]
    )

    if st.button(
        "Update Status"
    ):

        bed_df.loc[
            bed_df["bed_id"] == selected_bed,
            "status"
        ] = new_status

        bed_df.to_csv(
            "data/bed_management.csv",
            index=False
        )

        st.success(
            "Bed Status Updated"
        )

        st.rerun()

st.divider()

# ==================================
# Delete Bed
# ==================================

st.subheader("🗑 Delete Bed")

if not bed_df.empty:

    delete_bed = st.selectbox(
        "Select Bed ID",
        bed_df["bed_id"],
        key="delete_bed"
    )

    if st.button(
        "Delete Bed"
    ):

        bed_df = bed_df[
            bed_df["bed_id"] != delete_bed
        ]

        bed_df.to_csv(
            "data/bed_management.csv",
            index=False
        )

        st.success(
            "Bed Deleted Successfully"
        )

        st.rerun()

st.divider()

# ==================================
# Analytics
# ==================================

st.subheader("📈 Bed Analytics")

if not bed_df.empty:

    col1, col2 = st.columns(2)

    with col1:

        status_chart = px.pie(
            bed_df,
            names="status",
            title="Bed Occupancy Status"
        )

        st.plotly_chart(
            status_chart,
            use_container_width=True
        )

    with col2:

        type_chart = px.bar(
            bed_df["bed_type"]
            .value_counts()
            .reset_index(),
            x="bed_type",
            y="count",
            title="Beds by Type"
        )

        st.plotly_chart(
            type_chart,
            use_container_width=True
        )

st.divider()

# ==================================
# Bed Availability Alert
# ==================================

if available_beds < 5:

    st.error(
        "⚠ Critical Alert: Available beds are below threshold!"
    )

elif available_beds < 10:

    st.warning(
        "⚠ Bed availability is getting low."
    )

else:

    st.success(
        "✅ Bed availability is healthy."
    )