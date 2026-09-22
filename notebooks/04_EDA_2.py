import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])
#How does sales change over time?

#extracting year and month from invoice date
sales_df["YearMonth"] = sales_df["InvoiceDate"].dt.to_period("M")
print(sales_df[["InvoiceDate", "YearMonth"]].head())

#monthly revenue
print("Monthly revenue:")
monthly_revenue = (
    sales_df.groupby("YearMonth")["Revenue"]
    .sum()
)
print(monthly_revenue)

#monthly revenue plot/graph
monthly_revenue.plot(
    kind="line",
    figsize=(12, 5),
    title="Monthly Revenue"
)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

#highest monthly revenue
print("\nTop 5 months by revenue:")
print(monthly_revenue.sort_values(ascending=False).head(5))

#monthly trasactions
print("\nMonthly transactions:")
monthly_transactions = (
    sales_df.groupby("YearMonth")["Invoice"]
    .nunique()
)
print(monthly_transactions)
monthly_transactions.plot(
    kind="line",
    figsize=(12, 5),
    title="Monthly Number of Invoices"
)

plt.xlabel("Month")
plt.ylabel("Number of Invoices")
plt.show()

#comparing monthly revenue and transactions
print("Top months by revenue:")
print(monthly_revenue.sort_values(ascending=False).head(5))

print("\nTop months by number of invoices:")
print(monthly_transactions.sort_values(ascending=False).head(5))

#Days of the week analysis
sales_df["DayOfWeek"] = sales_df["InvoiceDate"].dt.day_name()
#here it shows the number of transactions for each day of the week and not unique invoices
print("\nNumber of transactions by day of the week (transactions not invoices):")
print(sales_df["DayOfWeek"].value_counts())

#Here we actually count the number of unique invoices for each day of the week
weekday_transactions = (sales_df.groupby("DayOfWeek")["Invoice"].nunique())
print("\nNumber of unique invoices by day of the week:")
print(weekday_transactions)

#putting the days of the week in order
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_df["DayOfWeek"] = pd.Categorical(
    sales_df["DayOfWeek"],
    categories=weekday_order,
    ordered=True
)
weekday_transactions = (
    sales_df.groupby("DayOfWeek", observed=False)["Invoice"]
    .nunique()
)
print("\nNumber of unique invoices by day of the week (ordered):")
print(weekday_transactions)
weekday_transactions.plot(
    kind="bar",
    figsize=(10, 5),
    title="Number of Invoices by Day of Week"
)

plt.xlabel("Day")
plt.ylabel("Number of Invoices")
plt.show()

#hourly analysis
sales_df["Hour"] = sales_df["InvoiceDate"].dt.hour
hourly_transactions = (
    sales_df.groupby("Hour")["Invoice"]
    .nunique()
)
print("\nNumber of unique invoices by hour:")
print(hourly_transactions)

hourly_transactions.plot(
    kind="line",
    marker="o",
    figsize=(10, 5),
    title="Number of Invoices by Hour"
)

plt.xlabel("Hour of Day")
plt.ylabel("Number of Invoices")
plt.xticks(range(0, 24))
plt.show()
