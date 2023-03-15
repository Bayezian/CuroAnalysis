"""
Script to return stacked bar chart illustrating number of repairs,
by year by quarter.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
repaironDemand = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory = False)

# Remove white space
repaironDemand["ContractorReference"] = repaironDemand[
    "ContractorReference"
].str.strip()

# Divide into DLO and non DLO repairs
cdata = repaironDemand[repaironDemand["ContractorReference"] == "000500"]
other = repaironDemand[repaironDemand["ContractorReference"] != "000500"]


def groupFunc(data: pd.DataFrame) -> pd.DataFrame:
    """
    Returns dataframe with required group-bys to plot
    """
    df = data.groupby(["FiscalYearLoggedDate", "FiscalQuarterLoggedDate"]).count()
    df = pd.DataFrame(df["order_no"])
    return df


rod = groupFunc(cdata)
other = groupFunc(other)

# print(rod.mean()) -> 9395.138889
# print(other.mean()) -> 1093.388889


def plotStack(data: pd.DataFrame, title: str) -> None:
    """
    Returns a stacked barchart from grouped-by dataframe
    """
    ax = data.unstack().plot(
        kind="bar", color=["#482173", "#2e6f8e", "#29af7f", "#bddf26"]
    )
    plt.axhline(y=9395.138889, color="r", linestyle="dotted")
    ax.title.set_text(title)
    ax.set_ylabel("Count")
    ax.set_xlabel("Sum of logged repairs by Quarter by Year")
    plt.legend(
        ["Mean repairs", "Q1", "Q2", "Q3", "Q4"],
        bbox_to_anchor=(1.05, 1.0),
        loc="upper left",
        title="Labels",
    )
    plt.tight_layout()
    plt.show()

# Call functions
# plotStack(rod, "Curo logged repairs by Year by Quarter (fiscal)")
# plotStack(other, "Other logged repairs by Year by Quarter (fiscal)")
