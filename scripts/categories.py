from utils import dlo_data as df
import pandas as pd

# Load data
repairs = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory=False)

# Strip white space from required columns
repairs["prty_id"] = repairs.prty_id.str.strip()
repairs["ContractorReference"] = repairs["ContractorReference"].str.strip()

# Get counts of repairs
counts = repairs.groupby("prty_id", as_index=False).size()
counts["prty_id"] = counts["prty_id"].str.strip()
df["prty_id"] = df["prty_id"].str.strip()
df = df.merge(counts, on="prty_id", how="left")

# Convert DateBuilt into datetime object
df["DateBuilt"] = pd.to_datetime(df["DateBuilt"])

# Get only years
# df["DateBuilt"] = df["DateBuilt"].dt.strftime("%Y")

# Plot repairs by year
# plt.title("High repair properties  (2015 - 2023)")
# df.groupby("DateBuilt")["prty_id"].count().sort_values(ascending = False)[:10].plot.bar()
# plt.xlabel("Construction date")
# plt.ylabel("Number of repairs")
# plt.show()

# Group the dataframe by decade and plot *NOTE this won't work if you run strftime("Y")

# df['decade'] = df['DateBuilt'].dt.year // 10 * 10
# plt.title("Houses constructed by decade")
# df.groupby('decade').size().plot.bar()
# plt.xlabel("Year")
# plt.ylabel("Count")
# plt.show()
