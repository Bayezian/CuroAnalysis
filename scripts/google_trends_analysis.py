"""
Analysing keyword analysis over time
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Numbers represent search interest relative to the highest point on the chart for the given region and time. 
A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. 
A score of 0 means that there was not enough data for this term.
"""

# Read in data
df = pd.read_csv(
    "/Users/bengroves/Desktop/curoAnalysis/data/trends/keyword_damp_terms - keyword_damp_terms.csv"
)

# Plot keyword trends over time
fig, ax = plt.subplots(figsize=[12, 7])
ax.plot(df["Month"], df[["mould", "black mould", "damp", "house mould", "house damp"]])
plt.title("Google keyword trends 2015 - 2023")
plt.xticks(np.arange(0, len(df["Month"].unique()), 10))
plt.legend(["Mould", "Black mould", "Damp", "House mould", "House damp"])
plt.show()
