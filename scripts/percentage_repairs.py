"""
Script to calculate the percentage of property ids logged in the repairs csv.
"""

from utils import dlo_data as df
import pandas as pd
import matplotlib.pyplot as plt

# Load data
repaironDemand = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory = False)

def perc(x: pd.Series, y: pd.Series) -> float:
    """
    Calculates percentage of unique property ids are found in joined repair data.
    """
    return (x.nunique() / len(y)) * 100

# Calculate percentage repairs
percRepairs = perc(repaironDemand["prty_id"], df["prty_id"])

# Set labels and attrs for plots
labels = ["Repaired", "Not repaired"]
sizes = [percRepairs, (100 - percRepairs)]
colors = ["green", "blue"]
explode = (0.1, 0)  # explode 1st slice

# Plot pie chart
fig1, ax1 = plt.subplots()
ax1.pie(
    sizes,
    labels=labels,
    explode=explode,
    autopct="%1.1f%%",
    colors=colors,
    shadow=True,
    startangle=90,
)
plt.axis("equal")
plt.show()
