"""
File to hold utility functions
"""

import pandas as pd

properties = pd.read_csv("../data/Property_Data.csv")


def filter_DLO_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Function to remove whitespace, filter data by live property, doesn't contain
    property codes and doesn't contain certain business streams
    """
    dataframe.columns = dataframe.columns.str.strip()
    dataframe["PropertyStatus"] = dataframe["PropertyStatus"].str.strip()
    dataframe = dataframe[dataframe["PropertyStatus"] == "Live Property"]
    dataframe = dataframe[~dataframe["prty_id"].str.contains("INTBL|EXTBL|ESTBL")]
    dataframe = dataframe[
        ~dataframe["BusinessStream"].str.contains(
            "Block|Commercial Properties|Garage|Office|Parking Space|Play/Communal Area"
        )
    ]

    return dataframe


dlo_data = filter_DLO_data(properties)
