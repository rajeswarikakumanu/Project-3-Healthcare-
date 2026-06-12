
# 🏥 AI-Powered Healthcare Prediction & Resource Management System

 WEBLINK:https://project-3-healthcare.onrender.com

An intelligent healthcare management system built using **Streamlit + Machine Learning** that helps hospitals predict diseases, manage patients, optimize resources, and improve treatment decisions.

---

## 🚀 Features

### 🔐 Authentication & User Management
- Patient / Doctor / Admin login system
- Role-based dashboards
- Secure user management

---

### 🧑 Patient Module
- Register and manage patient profiles
- View doctors and appointments
- Book appointments
- View medical history and notifications

---

### 👨‍⚕️ Doctor Module
- View assigned patients
- Manage appointment requests
- Approve / Reject appointments
- View patient medical details

---

### 📅 Appointment System
- Book appointments with doctors
- Doctor approval system
- Real-time status tracking (Pending / Approved / Rejected)

---

### 🩺 AI Disease Prediction
- Predict diseases using ML models
- Inputs: symptoms, age, BP, sugar, BMI
- Models: Random Forest, XGBoost, Decision Tree

---

### 💊 Treatment Recommendation
- AI-based treatment suggestions
- Medication recommendations
- Specialist suggestions

---

### 📈 Patient Outcome Prediction
- Recovery probability
- ICU requirement prediction
- Risk classification (High/Low)

---

### 🛏 Bed Management System
- Real-time bed availability tracking
- ICU bed monitoring
- Occupancy analytics

---

### 👩‍⚕️ Staff Management
- Staff scheduling system
- Shift allocation
- Workload distribution

---

### 🏥 Resource Management
- Manage hospital resources
- Predict resource demand
- Optimize usage

---

### 🧪 Medical Report Analysis
- Upload and analyze reports
- Detect abnormal values
- Generate risk alerts

---

### 🔔 Notification System
- Appointment notifications
- Emergency alerts
- Lab report alerts
- Stored using CSV (no database required)

---

### 📊 Analytics Dashboard
- Patient analytics
- Doctor analytics
- Hospital KPI dashboard
- Resource utilization charts

---

### 🤖 AI Chatbot
- Symptom checking assistant
- Appointment help
- Basic medical guidance

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend Logic:** Python
- **ML Models:** Scikit-learn, XGBoost
- **Data Handling:** Pandas, NumPy
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Storage:** CSV Files (No Database)
- **Model Saving:** Joblib

---

## 📂 Project Structure

```

Healthcare_AI_System/
│
├── app.py
├── pages/
├── utils/
├── data/
├── models/
├── requirements.txt
└── README.md

````

---

## 📦 Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/healthcare-ai-system.git
cd healthcare-ai-system
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Application

```bash
streamlit run app.py
```

---

## 📊 Data Storage

This project uses **CSV-based storage (no database required)**:

* patients.csv
* doctors.csv
* appointments.csv
* notifications.csv
* bed_management.csv
* resources.csv

---

## 📌 Key Highlights

* No database required (fully file-based system)
* AI-powered predictions
* Real-time appointment approval system
* Role-based dashboards
* Interactive analytics dashboard

---

## 🚀 Future Improvements

* Add real database (MySQL / MongoDB)
* Deploy AI models using API
* Add real SMS/Email notifications
* Improve chatbot with LLM integration
* Mobile application support

---

## 👨‍💻 Author

**Rajeswari Kakumanu**

---
