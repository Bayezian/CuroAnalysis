"""
File containing code for pearson correlation coefficient analysis
"""

import pandas as pd
from utils import dlo_data as df
import matplotlib.pyplot as plt
import numpy as np

# Load data
repairs = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory=False)

# Strip white space from required columns
repairs["prty_id"] = repairs["prty_id"].str.strip()
repairs["ContractorReference"] = repairs["ContractorReference"].str.strip()

# counts = repaironDemand.groupby('prty_id', as_index=False).size().sort_values(by = "size", ascending= False)
counts = repairs.groupby("prty_id", as_index=False).size()
counts["prty_id"] = counts["prty_id"].str.strip()
df["prty_id"] = df["prty_id"].str.strip()


# One hot encode categorical columns
ohe = pd.get_dummies(
    df[["TenancyType", "ConstructionType", "ConstructionStyle", "PropertyStatus"]]
)
df = df.drop(
    columns=["TenancyType", "ConstructionType", "ConstructionStyle", "PropertyStatus"]
)
df = df.join(ohe)
df = df.merge(counts, on="prty_id", how="left")
df = df.fillna(0)

# Rename column for ease
df = df.rename(columns={"size": "number_of_repairs"})

# Create yearBuilt feature
t = df.DateBuilt.str.split("-", expand=True)
df["yearBuilt"] = t[0]
df = df.dropna()
df["yearBuilt"] = df["yearBuilt"].str.strip()

# Groupby number of repairs
pc = df.groupby("prty_id", as_index=False)["number_of_repairs"].count()

# Get list of high repair properties
pc["prty_id"].sort_values(ascending=False)[:15].to_list()

# Fill remaining NAs
repairs = repairs.fillna(0)

# List of high properties
# high_repair_properties = ['ZFTATRUST235', 'YORIHO0000', 'WYCLRO_8_TO_9_EXTBL', 'WYCLRO_6_TO_7_EXTBL', 'WYCLRO_4_TO_5_EXTBL', 'WYCLRO_1_TO_3_EXTBL', 'WYCLRO_1_TO_11_SRVBL', 'WYCLRO_1_TO_11_ESTBL', 'WYCLRO_10_TO_11_EXTBL', 'WYCLRO0011', 'WYCLRO0010', 'WYCLRO0009', 'WYCLRO0008', 'WYCLRO0007', 'WYCLRO0006']

# For some reason had to add as list not variable containing list
# df = df[df["prty_id"].isin(['ZFTATRUST235', 'YORIHO0000', 'WYCLRO_8_TO_9_EXTBL', 'WYCLRO_6_TO_7_EXTBL', 'WYCLRO_4_TO_5_EXTBL', 'WYCLRO_1_TO_3_EXTBL', 'WYCLRO_1_TO_11_SRVBL', 'WYCLRO_1_TO_11_ESTBL', 'WYCLRO_10_TO_11_EXTBL', 'WYCLRO0011', 'WYCLRO0010', 'WYCLRO0009', 'WYCLRO0008', 'WYCLRO0007', 'WYCLRO0006'])]

# Drop unneeded features
df = df.drop(columns=["northing", "easting"], axis=1)

# Take top 5 correlations and plot
# plt.title("5 most correlated features of high repair properties")
# df.corr()["number_of_repairs"].sort_values(ascending=False)[1:6].plot.bar()
# plt.xlabel("Feature")
# plt.ylabel("Count")
# plt.show()

# Plot by year, however with filters this doesn't do much.
# plt.title("Property repair by construction date")
# df.groupby('yearBuilt')['number_of_repairs'].sum().plot.bar()
# plt.xticks(np.arange(0, len(df["yearBuilt"].unique()), 10))
# plt.show()


# Plot properties by build date count
# count_data = df["yearBuilt"].value_counts().sort_values(ascending = False)
# plt.title("Properties by build date (top 10)")
# plt.xlabel("Year")
# plt.ylabel("Count")
# count_data[:10].plot.bar()
# plt.show()


# # Plot correlations for properties built in 2011. Can be changed for any year
# df["yearBuilt"] = df["yearBuilt"].str.strip()
# df = df[df["yearBuilt"] == "2011"]
# corr = df.corr()["number_of_repairs"].sort_values(ascending = False)
# plt.title("Constructed in 2011 correlation with number of repairs (Pearson)")
# plt.xlabel("Property feature")
# plt.ylabel("Pearson Coefficient")
# corr[1:11].plot.bar()
# plt.show()
