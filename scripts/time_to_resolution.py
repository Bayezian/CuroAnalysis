"""
Scripts for time to resolution calculations
"""

import pandas as pd
import matplotlib.pyplot as plt

# Import data
repaironDemand = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory=False)

# Fill NA values that mess with later analysis
repaironDemand = repaironDemand.fillna(0)

# Cast fiscal year completed data as integers
repaironDemand["FiscalYearCompletedDate"] = repaironDemand[
    "FiscalYearCompletedDate"
].astype(int)
repaironDemand["MonthNumberCompletedDate"] = repaironDemand[
    "MonthNumberCompletedDate"
].astype(int)

#  Create DMY feature
t = (
    "01-"
    + repaironDemand["MonthNumberLoggedDate"].astype(str)
    + "-"
    + repaironDemand["FiscalYearLoggedDate"].astype(str)
)
v = (
    "01-"
    + repaironDemand["MonthNumberCompletedDate"].astype(str)
    + "-"
    + repaironDemand["FiscalYearCompletedDate"].astype(str)
)

# Replace all 0s with an arbitrary date
v = v.replace({"0-0": "01-1850"}, regex=True)

# Convert new features into datetime objects
df = pd.DataFrame(
    {
        "date_logged": t.apply(lambda x: pd.to_datetime(x)),
        "date_finished": v.apply(lambda x: pd.to_datetime(x)),
    }
)

# Create a time to completion feature
df["ttc"] = df["date_finished"] - df["date_logged"]

# Add logged date to df
df["year"] = repaironDemand["FiscalYearLoggedDate"]

# Groupby statement to get counts per year
time = df.groupby("year", as_index=False)["ttc"].value_counts()

# This says days but refers to months. This is just due to the pandas datetime nonenclature
x = time[time["ttc"] == "0 days"]
y = time[time["ttc"] == "1 days"]
z = time[time["ttc"] == "3 days"]

"""
Every single entry is set to first of each month by default.
Therefore, if there is a 0 day ttc the order has been completed
in the same month that it has been logged.
One day would mean that the repair is closed one month after creation and so on.

basically - days should be month. The ttc start and end month are the same.
"""

# Merge the different ttc's into one dataframe
t = x.merge(y, on="year")
p = t.merge(z, on="year")

# Plot time to completion over time
fig, ax = plt.subplots(figsize=[12, 7])
ax.plot(p["year"], p[["count_x", "count_y", "count"]])
plt.title("Time to resolution counts by year")
plt.xlabel("Date")
plt.legend(["Same month", "1 month", "3 month"])
plt.show()
