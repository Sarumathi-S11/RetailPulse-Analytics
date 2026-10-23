
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "data/raw/superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

print("=== RETAILPULSE ANALYTICS ===")
print("\n1. Original dataset shape:", df.shape)

# Clean column names
df.columns = df.columns.str.strip()

# Convert dates into datetime format
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="mixed"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="mixed"
)

# Remove duplicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

print("2. Duplicate rows found:", duplicates)
print("3. Dataset shape after cleaning:", df.shape)
print("4. Missing values:", df.isnull().sum().sum())

# Business summary
print("\n=== BUSINESS SUMMARY ===")
print("Total Sales: $", round(df["Sales"].sum(), 2))
print("Total Profit: $", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order ID"].nunique())
print("Total Customers:", df["Customer ID"].nunique())

# Sales by category
print("\n=== SALES BY CATEGORY ===")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales.sort_values(ascending=False))

# Profit by region
print("\n=== PROFIT BY REGION ===")
region_profit = df.groupby("Region")["Profit"].sum()
print(region_profit.sort_values(ascending=False))

# Monthly sales trend
df["Order Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Order Month")["Sales"].sum()

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/superstore_cleaned.csv", index=False)
monthly_sales.to_csv("data/processed/monthly_sales.csv")

# Save monthly sales chart
os.makedirs("reports", exist_ok=True)
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/monthly_sales_trend.png")
plt.close()

print("\n5. Cleaned dataset saved to data/processed/")
print("6. Monthly sales chart saved to reports/monthly_sales_trend.png")
print("\nDay 2 analysis completed successfully!")
