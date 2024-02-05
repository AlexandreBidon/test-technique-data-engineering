import pandas as pd
from typing import List
import re
import logging


def remove_artefact(df: pd.DataFrame, column_list: List[str]):
    """
    Removes the artefact appearing because of string conversion.
    """
    for column in column_list:
        # Checks if the column is in the dataframe
        if column in df.columns:
            df[column].apply(lambda x: re.sub(r'[^\x00-\x7f]',r'', x))
            logging.debug("Successfully removed artefact from column {}".format(column))
            print(df[column])
        else:
            # Log to warn the user about the problem
            # Another solution would be to return an error
            logging.warning("Could not find column {} while removing artefact.".format(column))
    return df