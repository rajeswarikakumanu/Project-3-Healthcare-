import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Healthcare System Login")

# Create users.csv automatically if it doesn't exist
if not os.path.exists("data/users.csv"):
    users = pd.DataFrame({
        "user_id": [1, 2, 3],
        "username": ["admin", "doctor1", "patient1"],
        "password": ["admin123", "doctor123", "patient123"],
        "role": ["Admin", "Doctor", "Patient"]
    })
    users.to_csv("data/users.csv", index=False)

users_df = pd.read_csv("data/users.csv")

tab1, tab2 = st.tabs(["Login", "Register"])

# ---------------- LOGIN ----------------
with tab1:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = users_df[
            (users_df["username"] == username) &
            (users_df["password"] == password)
        ]

        if not user.empty:

            role = user.iloc[0]["role"]

            st.success(f"Welcome {username}")
            st.info(f"Role: {role}")

            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role

        else:
            st.error("Invalid Username or Password")

# ---------------- REGISTER ----------------
with tab2:

    st.subheader("New User Registration")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    role = st.selectbox(
        "Role",
        ["Patient", "Doctor"]
    )

    if st.button("Register"):

        if new_username in users_df["username"].values:
            st.warning("Username already exists")

        else:

            new_user = {
                "user_id": len(users_df) + 1,
                "username": new_username,
                "password": new_password,
                "role": role
            }

            users_df = pd.concat(
                [users_df, pd.DataFrame([new_user])],
                ignore_index=True
            )

            users_df.to_csv(
                "data/users.csv",
                index=False
            )

            st.success("Registration Successful")