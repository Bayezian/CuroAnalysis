"""
Plotting by year and categories
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data in
df = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory = False)

def renderSubplots(data: pd.DataFrame, labelOne: str, labelTwo: str) -> None:
    """
    Function to render repairs by month, by date
    """
    fig, ax = plt.subplots(1, 2)

    # By month
    sns.countplot(
        data=data,
        x="MonthNameLoggedDate",
        ax=ax[0],
        palette=["#482173", "#2e6f8e", "#29af7f", "#bddf26"],
    )

    # By year

    sns.countplot(
        data=data,
        x="FiscalYearLoggedDate",
        ax=ax[1],
        palette=["#482173", "#2e6f8e", "#29af7f", "#bddf26"],
    )

    ax[0].set_xlabel("Sum of logged repairs by Month")
    ax[0].set_ylabel("Count")

    ax[1].set_xlabel("Sum of logged repairs by Year")
    ax[1].set_ylabel("Count")

    ax[0].tick_params(axis="x", labelrotation=90)

    ax[0].title.set_text(labelOne)
    ax[1].title.set_text(labelTwo)
    plt.show()


renderSubplots(df, "DLO repairs by Month", "DLO repairs by Year")
# renderSubplots(otherOrders, "Other order repairs by Month", "Other order repairs by Year")
