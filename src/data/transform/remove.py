from typing import List
import logging
import pandas as pd



def remove_columns(df: pd.DataFrame, column_list: List[str]):
    for column in column_list:
        if column in df.columns:
            logging.debug("Deleting column named %s",column)
            df = df.drop(column, axis=1)
        else:
            logging.warning("Could not delete column named %s",column)
    return df
