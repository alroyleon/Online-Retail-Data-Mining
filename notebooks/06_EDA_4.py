#Customer Analysis
import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])
customer_df = sales_df.dropna(subset=["Customer ID"]).copy()

#grouping by customer ID to get the number of unique customers
print(f"Number of unique customers: {customer_df['Customer ID'].nunique()}")
customer_orders = (
    customer_df.groupby("Customer ID")["Invoice"]
    .nunique()
    .sort_values(ascending=False)
)
print("Top Customers by Number of Orders:")
print(customer_orders.head(10))

customer_quantity = (
    customer_df.groupby("Customer ID")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
print("Top Customers by Total Quantity Purchased:")
print(customer_quantity.head(10))

customer_revenue = (
    customer_df.groupby("Customer ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("Top Customers by Revenue:")
print(customer_revenue.head(10))
customer_revenue.head(10).sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Top 10 Customers by Revenue"
)
plt.xlabel("Revenue")
plt.ylabel("Customer ID")
plt.show()

#Summary table
customer_summary = (
    customer_df.groupby("Customer ID")
    .agg(
        NumberOfOrders=("Invoice", "nunique"),
        UnitsPurchased=("Quantity", "sum"),
        TotalRevenue=("Revenue", "sum"),
        AverageUnitPrice=("Price", "mean"),
        TransactionLines=("Invoice", "size")
    )
)
print(customer_summary.head())

customer_summary["AverageOrderValue"] = (
    customer_summary["TotalRevenue"] /
    customer_summary["NumberOfOrders"]
)
print(customer_summary.head())

#Statistical Summary of customer spending
print("Distribution of Customer Spending:")
print(customer_summary["TotalRevenue"].describe())
print(customer_summary["NumberOfOrders"].describe())
print(customer_summary["AverageOrderValue"].describe())

#Comparing top customers
print("Top Customers by Revenue:")
print(customer_summary.sort_values(
    "TotalRevenue",
    ascending=False
).head(10))
print("Top Customers by Number of Orders:")
print(customer_summary.sort_values(
    "NumberOfOrders",
    ascending=False
).head(10))
print("Top Customers by Units Purchased:")
print(customer_summary.sort_values(
    "UnitsPurchased",
    ascending=False
).head(10))

#How concentrated is customer revenue?
customer_revenue_sorted = (
    customer_summary["TotalRevenue"]
    .sort_values(ascending=False)
)
total_customer_revenue = customer_revenue_sorted.sum()
print(f"Total Revenue from all customers: {total_customer_revenue}")
customer_cumulative = customer_revenue_sorted.cumsum()
customer_cumulative_percentage = (
    customer_cumulative /
    total_customer_revenue *
    100
)
customers_for_80 = (
    customer_cumulative_percentage <= 80
).sum()

print(f"Number of customers contributing to 80% of total revenue: {customers_for_80}")
customer_summary["TotalRevenue"].plot(
    kind="hist",
    bins=50,
    figsize=(10, 5),
    title="Distribution of Customer Revenue"
)

plt.xlabel("Total Revenue per Customer")
plt.ylabel("Number of Customers")
plt.show()

customer_summary.plot(
    kind="scatter",
    x="NumberOfOrders",
    y="TotalRevenue",
    figsize=(10, 6),
    title="Customer Orders vs Total Revenue"
)

plt.xlabel("Number of Orders")
plt.ylabel("Total Revenue")
plt.show()

#Final data
print(customer_df.shape)
print(customer_df["Customer ID"].nunique())
print(customer_summary.describe())
print(customer_summary.sort_values(
    "TotalRevenue",
    ascending=False
).head(10))
print(f"Number of customers contributing to 80% of total revenue: {customers_for_80}")