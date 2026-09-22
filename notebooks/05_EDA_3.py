#Product Analysis
import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv("D:/data_mining/data/processed/cleaned_transactions.csv",parse_dates=["InvoiceDate"])

#top products by quantity sold
