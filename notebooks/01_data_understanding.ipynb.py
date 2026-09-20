"""
Load raw data
    ↓
Investigate missing values
    ↓
Investigate anomalies
    ↓
Remove bad-debt adjustments
    ↓
Remove cancellation invoices
    ↓
Remove non-positive sales
    ↓
Remove exact duplicates
    ↓
Create Revenue
    ↓
Export cleaned_transactions.csv

"""
import pandas as pd
df = pd.read_excel("D:/data_mining/data/raw/online_retail_II.xlsx")
#cloning to make changes
sales_df = df.copy()

#Remove accounting adjustments
sales_df = sales_df[sales_df["Description"] != "Adjust bad debt"]

#Remove cancelled invoices
sales_df = sales_df[~sales_df["Invoice"].astype(str).str.startswith("C")]

#Keep only actual positive sales
sales_df = sales_df[(sales_df["Quantity"] > 0) & (sales_df["Price"] > 0)]

#Remove exact duplicate rows
sales_df = sales_df.drop_duplicates()

#Reset the index
sales_df = sales_df.reset_index(drop=True)

#rechecking after cleaning
print((sales_df.isnull()).sum())
print("Negative quantities:", (sales_df["Quantity"] < 0).sum())
print("Zero quantities:", (sales_df["Quantity"] == 0).sum())
print("Negative prices:", (sales_df["Price"] < 0).sum())
print("Zero prices:", (sales_df["Price"] == 0).sum())
print("Cancelled invoices:", sales_df["Invoice"].astype(str).str.startswith("C").sum())
print("Duplicates:", sales_df.duplicated().sum())

#creating revenue column (new column)
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["Price"]
#checking the new column
print("Revenue column:")
print(sales_df[["Quantity", "Price", "Revenue"]].head())

sales_df.to_csv("D:/data_mining/data/processed/cleaned_transactions.csv",index=False)