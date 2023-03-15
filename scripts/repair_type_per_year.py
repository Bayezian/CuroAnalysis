"""
Repair types per year
"""

import pandas as pd
import matplotlib.pyplot as plt

repaironDemand = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory=False)

# Remove white space from Contractor reference column
repaironDemand["ContractorReference"] = repaironDemand[
    "ContractorReference"
].str.strip()

# Get only Curo repair codes
repaironDemand = repaironDemand[
    repaironDemand["ContractorReference"].isin(["000500", "007809", "007865"])
]

# Groupby statement to get counts per fiscal year
df = repaironDemand.groupby(["FiscalYearLoggedDate"], as_index=False)[
    "TradeDesn"
].value_counts()

# Remove white space from cols and column
df.columns = df.columns.str.strip()
df["TradeDesn"] = df["TradeDesn"].str.strip()

# Filter dataframe by key TradeDesn
carpentry = df[df["TradeDesn"] == "Carpentry"]
electrical = df[df["TradeDesn"] == "Electrical"]
plumbing = df[df["TradeDesn"] == "Plumbing"]

# Merge them together into single dataframe
x = carpentry.merge(electrical, on="FiscalYearLoggedDate")
y = x.merge(plumbing, on="FiscalYearLoggedDate")

# Calculate percentage changes by year
# y["count_x"] = y["count_x"].pct_change()
# y["count_y"] = y["count_y"].pct_change()
# y["count"] = y["count"].pct_change()

# Plotting change in TradeDesn over time
plt.title("Change in trade jobs over time")
colors = ["#bddf26", "#2e6f8e", "#29af7f"]
plt.xlabel("Year")
plt.ylabel("Count")
plt.gca().set_prop_cycle(color=colors)
plt.plot(y["FiscalYearLoggedDate"], y[["count_x", "count_y", "count"]])
plt.legend(["Carpentry", "Electrical", "Plumbing"])
plt.show()
