import pandas as pd
import os

USERS_FILE = "data/users.csv"


def authenticate_user(username, password):

    if not os.path.exists(USERS_FILE):
        return None

    users = pd.read_csv(USERS_FILE)

    user = users[
        (users["username"] == username)
        &
        (users["password"] == password)
    ]

    if not user.empty:

        return {
            "username": user.iloc[0]["username"],
            "role": user.iloc[0]["role"]
        }

    return None


def register_user(
    username,
    password,
    role
):

    if not os.path.exists(USERS_FILE):

        users = pd.DataFrame(columns=[
            "user_id",
            "username",
            "password",
            "role"
        ])

    else:

        users = pd.read_csv(USERS_FILE)

    if username in users["username"].values:
        return False

    new_user = {
        "user_id": len(users) + 1,
        "username": username,
        "password": password,
        "role": role
    }

    users = pd.concat(
        [users, pd.DataFrame([new_user])],
        ignore_index=True
    )

    users.to_csv(
        USERS_FILE,
        index=False
    )

    return True