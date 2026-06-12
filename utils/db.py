import pandas as pd
import os

def load_csv(file_path):
    """
    Load CSV file safely.
    """

    if os.path.exists(file_path):
        return pd.read_csv(file_path)

    return pd.DataFrame()


def save_csv(df, file_path):
    """
    Save dataframe to CSV.
    """

    df.to_csv(
        file_path,
        index=False
    )


def append_csv(new_data, file_path):
    """
    Append record to CSV.
    """

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        df = pd.concat(
            [df, pd.DataFrame([new_data])],
            ignore_index=True
        )

    else:

        df = pd.DataFrame([new_data])

    df.to_csv(
        file_path,
        index=False
    )