import pandas as pd

print("Starting ETL Pipeline...")

# Load raw dataset
df = pd.read_csv("data/Superstore.csv", encoding="latin1")

# Standardize column names
df.columns = [c.lower().replace(" ", "_") for c in df.columns]

# Convert dates
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# Feature Engineering
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# Profit Margin KPI
df["profit_margin"] = (df["profit"] / df["sales"]) * 100

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/cleaned_superstore.csv", index=False)

print("ETL Completed Successfully!")
print("Cleaned dataset saved at: data/cleaned_superstore.csv")
