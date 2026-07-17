import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> bool:
    return not df.empty and not df.columns.duplicated().any()
