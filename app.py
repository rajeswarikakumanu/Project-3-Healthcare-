import streamlit as st

st.set_page_config(
    page_title="AI-Powered Healthcare Prediction & Resource Management System",
    page_icon="🏥",
    layout="wide"
)

# ====================================
# Header
# ====================================

st.title("🏥 AI-Powered Healthcare Prediction & Resource Management System")

st.markdown("""
Welcome to the AI-Powered Healthcare Prediction & Resource Management System.

This platform helps hospitals and healthcare providers:

- Predict disease risks
- Recommend treatments
- Predict patient outcomes
- Manage beds and resources
- Schedule staff efficiently
- Analyze medical reports
- Monitor healthcare analytics
""")

st.divider()

# ====================================
# System Overview
# ====================================

st.subheader("📌 System Modules")

modules = [
    "🔐 Login & User Management",
    "🧑 Patient Dashboard",
    "👨‍⚕️ Doctor Dashboard",
    "🏥 Admin Dashboard",
    "📅 Appointment Scheduling",
    "🩺 Disease Prediction",
    "💊 Treatment Recommendation",
    "📈 Outcome Prediction",
    "🛏 Bed Management",
    "👩‍⚕️ Staff Management",
    "🏥 Resource Management",
    "🧪 Medical Report Analysis",
    "🤖 AI Chatbot",
    "📊 Analytics Dashboard"
]

for module in modules:
    st.write(module)

st.divider()

# ====================================
# Key Features
# ====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 🩺 AI Disease Prediction
    
    - Diabetes Risk
    - Heart Disease Risk
    - Health Assessment
    """)

with col2:
    st.success("""
    ### 🏥 Hospital Management
    
    - Bed Tracking
    - Resource Allocation
    - Staff Scheduling
    """)

with col3:
    st.warning("""
    ### 📊 Analytics
    
    - KPI Monitoring
    - Risk Analysis
    - Utilization Reports
    """)

st.divider()

# ====================================
# Workflow
# ====================================

st.subheader("🔄 Healthcare Workflow")

st.markdown("""
1. Register/Login
2. Manage Patients
3. Schedule Appointments
4. Predict Diseases
5. Generate Treatment Recommendations
6. Predict Patient Outcomes
7. Manage Beds & Resources
8. Analyze Reports
9. Monitor Analytics Dashboard
""")

st.divider()

# ====================================
# Project Statistics
# ====================================

st.subheader("📈 System Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Modules",
        "14"
    )

with col2:
    st.metric(
        "Dashboards",
        "3"
    )

with col3:
    st.metric(
        "AI Components",
        "4"
    )

with col4:
    st.metric(
        "Data Storage",
        "CSV Files"
    )

st.divider()

# ====================================
# Footer
# ====================================

st.success(
    "✅ System Ready. Use the sidebar to navigate between modules."
)

st.caption(
    "AI-Powered Healthcare Prediction & Resource Management System | Streamlit + Machine Learning"
)