import pandas as pd
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])
print(sales_df.head())
print(sales_df.shape)