import pandas as pd

# Load all 3 CSV files
#df1 = pd.read_csv("data/daily_sales_data_0.csv")
#df2 = pd.read_csv("data/daily_sales_data_1.csv")
#df3 = pd.read_csv("data/daily_sales_data_2.csv")
data = {
    "product": ["pink morsel", "pink morsel"],
    "price": ["$10", "$20"],
    "quantity": [2, 3],
    "date": ["2024-01-01", "2024-01-02"],
    "region": ["north", "south"]
}

df = pd.DataFrame(data)

# Combine all data
#df = pd.concat([df1, df2, df3])

# Filter only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove '$' from price and convert to float
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]

# Select required columns
output = df[["sales", "date", "region"]]

# Save output
output.to_csv("output.csv", index=False)

print("Task completed! Output saved as output.csv")