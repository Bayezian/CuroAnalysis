import pandas as pd
from utils import dlo_data as df
import matplotlib.pyplot as plt

# Import data
repairs = pd.read_csv("../data/Repairs_Demand_Orders.csv", low_memory=False)

# Remove whitespace from column headers
repairs.columns = repairs.columns.str.strip()

# Remove whitespace from prty_id columns
df.prty_id = df["prty_id"].str.strip()
repairs.prty_id = repairs["prty_id"].str.strip()

# Remove white space from columns to be queried
repairs["ContractorReference"] = repairs["ContractorReference"].str.strip()
repairs["message1"] = repairs["message1"].str.strip()

# Filter repairs by prty_id found in property ids
repairs = repairs[repairs["prty_id"].isin(df["prty_id"])]
dlo_codes = ["000500", "007809", "007865"]
repairs = repairs[repairs["ContractorReference"].isin(dlo_codes)]

# Get number of repairs by property
counts = repairs.groupby("prty_id", as_index=False).size()

# Left join number of repairs into property dataset
df = df.merge(counts, on="prty_id", how="left")

# Convert DateBuilt feature into pandas datetime object
df["DateBuilt"] = pd.to_datetime(df["DateBuilt"])

# Cast free text entries into type str
repairs["WorkTypeDescription"] = repairs["WorkTypeDescription"].apply(lambda x: str(x))
repairs["message1"] = repairs["message1"].apply(lambda x: str(x))
repairs["message2"] = repairs["message2"].apply(lambda x: str(x))

# Convert all free text entries into lower case
repairs["message1"] = repairs["message1"].apply(lambda x: x.lower())
repairs["message2"] = repairs["message2"].apply(lambda x: x.lower())


# Query selected columns for keywords
damp = repairs[
    repairs["message1"].str.contains(
        "mould growth|damp mould|mould|black mould|damp|house mould|fungus|black fungus|house damp",
        case=False,
    )
].index
leaks = repairs[repairs["message1"].str.contains("leak|leaks", case=False)].index
roof = repairs[repairs["message1"].str.contains("rooves|roof", case=False)].index

# Select repair rows containing only keywords
damp = repairs.loc[damp]
leaks = repairs.loc[leaks]
roof = repairs.loc[roof]

# Plot damp, leak and roof prevelance
# colors= ["#bddf26", "#2e6f8e", "#29af7f"]
# plt.gca().set_prop_cycle(color=colors)
# d = damp.groupby("FiscalYearLoggedDate")["order_no"].count()
# l = leaks.groupby("FiscalYearLoggedDate")["order_no"].count()
# r = roof.groupby("FiscalYearLoggedDate")["order_no"].count()
# plt.title(f"DLO repairs per keyword")
# plt.xlabel("Year")
# plt.ylabel("Count")
# d.plot()
# l.plot()
# r.plot()
# plt.legend(["Damp", "Leaks", "Roof"])
# plt.show()

# Join damp properties on property
# d = pd.merge(df, damp, on = "prty_id")

# Plot damp counts repairs by location
# plt.title("Properties with damp repairs by location")
# d["add_2"].value_counts()[:10].sort_values(ascending = False).plot.bar()
# plt.xlabel("Location")
# plt.ylabel("Count")
# plt.show()

# Plot repairs by post code (if given)
# plt.title("Sum number of repairs in properties with reported mould repairs by post code")
# d["post_code"] = d["post_code"].str.strip()
# d["post_code"].value_counts()[:10].sort_values(ascending = False).plot.bar()
# plt.xlabel("Post code")
# plt.ylabel("Count")
# plt.show()
