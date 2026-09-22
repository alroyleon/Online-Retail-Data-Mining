import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])
#Which countries generate the most revenue?
country_revenue = (
    sales_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 countries by revenue:")
print(country_revenue.head(10))

country_revenue.head(10).plot(
    kind="bar",
    figsize=(10, 5),
    title="Top 10 Countries by Revenue"
)
plt.show()


