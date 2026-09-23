#Product Analysis
import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])

#top products by quantity sold
product_quantity = (
    sales_df.groupby(["StockCode", "Description"])["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("Top Products by Quantity Sold:")
print(product_quantity.head(10))

#graph of top products by quantity sold
product_quantity.head(10).sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Top 10 Products by Quantity Sold"
)

plt.xlabel("Units Sold")
plt.ylabel("Product")
plt.show()

#top products by revenue
product_revenue = (
    sales_df.groupby(["StockCode", "Description"])["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("Top Products by Revenue:")
print(product_revenue.head(10))

#graph of top products by revenue
product_revenue.head(10).sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    title="Top 10 Products by Revenue"
)

plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

#comparing top products by quantity sold and revenue
print("Top Products by Quantity Sold:")
print(product_quantity.head(10))
print("\nTop Products by Revenue:")
print(product_revenue.head(10))

product_summary = (
    sales_df.groupby(["StockCode", "Description"])
    .agg(
        UnitsSold=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        AveragePrice=("Price", "mean")
    )
    .sort_values("UnitsSold", ascending=False)
)

print("Product Summary:")
print(product_summary.head(10))

#highest value products
print("Highest Value Products:")
print(product_summary.sort_values(
    "Revenue",
    ascending=False
).head(10))

#comparing revenue with units sold
print("Products with Highest Units Sold:")
print(product_summary.sort_values(
    "UnitsSold",
    ascending=False
).head(10))

#comparing top 10 revenue to total revenue to see the contribution of top products to overall revenue
total_revenue = sales_df["Revenue"].sum()
top_10_revenue = product_summary["Revenue"].head(10).sum()

top_10_percentage = (top_10_revenue / total_revenue) * 100

print(f"Percentage of total revenue contributed by top 10 products: {top_10_percentage:.2f}%")

#number of products contributing to 80% of revenue
revenue_sorted = product_summary.sort_values(
    "Revenue",
    ascending=False
).copy()
revenue_sorted["CumulativeRevenue"] = (
    revenue_sorted["Revenue"].cumsum()
)
revenue_sorted["CumulativePercentage"] = (
    revenue_sorted["CumulativeRevenue"] / total_revenue * 100
)
products_for_80 = (
    revenue_sorted["CumulativePercentage"] <= 80
).sum()

print(f"Number of products contributing to 80% of revenue: {products_for_80}")

#graph of cumulative revenue contribution by product
revenue_sorted["CumulativePercentage"].plot(
    figsize=(10, 5),
    title="Cumulative Revenue Contribution by Product"
)

plt.xlabel("Products (ranked by revenue)")
plt.ylabel("Cumulative Revenue (%)")
plt.axhline(80, linestyle="--")
plt.show()

