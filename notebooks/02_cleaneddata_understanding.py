import pandas as pd
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])
print(sales_df.head())
print(sales_df.shape)

#Basic Statistics to understand the unique transactions/invoices in the dataset
print("Number of transaction lines:",len(sales_df))
print("Number of unique invoices:",sales_df["Invoice"].nunique())
print("Number of unique stock codes:",sales_df["StockCode"].nunique())
print("Number of unique customer IDs:",sales_df["Customer ID"].nunique())
print("Number of unique countries:",sales_df["Country"].nunique())
print("Total quantity sold:",sales_df["Quantity"].sum())
print("Total revenue:",sales_df["Revenue"].sum())
print("Average revenue per transaction:",sales_df["Revenue"].mean())

#Time period covered in the dataset
print("Minimum invoice date:", sales_df["InvoiceDate"].min())
print("Maximum invoice date:", sales_df["InvoiceDate"].max())
print("Invoice date statistics:")
sales_df["InvoiceDate"].describe()

#checking if invoice date is datetime datatype in cleaned dataset
print("Data types:")
print(sales_df.dtypes)

#all the above in dataframe format
summary = pd.DataFrame({
    "Metric": [
        "Transaction lines",
        "Unique invoices",
        "Unique products",
        "Unique customers",
        "Countries",
        "Total quantity sold",
        "Total revenue",
        "Average line revenue"
    ],
    "Value": [
        len(sales_df),
        sales_df["Invoice"].nunique(),
        sales_df["StockCode"].nunique(),
        sales_df["Customer ID"].nunique(),
        sales_df["Country"].nunique(),
        sales_df["Quantity"].sum(),
        sales_df["Revenue"].sum(),
        sales_df["Revenue"].mean()
    ]
})

print(summary)
