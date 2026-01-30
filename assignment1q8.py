import pandas as pd # Import as pd

# Provided data [cite: 94-108]
data_dict = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create DataFrame
df = pd.DataFrame(data_dict)

# add new column D, created from existing columns
df["D"] = df["A"] * df["B"]

print(df)