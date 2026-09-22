import pandas as pd
df=pd.read_csv("/home/ashwel/git/Online-Retail-Data-Mining/data/processed/cleaned_transactions.csv")
print(df.head())
print(df.shape)
print(df.dtypes)

df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
print(df["InvoiceDate"].min())
print(df["InvoiceDate"].max())

df["Revenue"]=df["Quantity"]*df["Price"]
print(df[["Quantity","Price","Revenue"]].head())

rfm_data=df[(df["Quantity"]>0)&(df["Price"]>0)&(df["Customer ID"].notna())].copy()
print(rfm_data.shape)

analysis_date=rfm_data["InvoiceDate"].max()+pd.Timedelta(days=1)
print(analysis_date)
rfm=rfm_data.groupby("Customer ID").agg(Recency=("InvoiceDate",lambda x:(analysis_date-x.max()).days),Frequency=("Invoice","nunique"),Monetary=("Revenue","sum"))
print(rfm.head())

rfm=rfm.reset_index()
print(rfm.head())

quantity=rfm_data.groupby("Customer ID")["Quantity"].sum()
rfm["TotalQuantity"]=rfm["Customer ID"].map(quantity)

unique_products=rfm_data.groupby("Customer ID")["StockCode"].nunique()
rfm["UniqueProducts"]=rfm["Customer ID"].map(unique_products)

rfm["AverageOrderValue"]=rfm["Monetary"]/rfm["Frequency"]

print(rfm.shape)
print(rfm.isnull().sum())
print(rfm.describe())

print((rfm["Monetary"]<=0).sum())
print((rfm["Frequency"]<=0).sum())
print((rfm["Recency"]<=0).sum())

rfm.to_csv("/home/ashwel/git/Online-Retail-Data-Mining/data/processed/customer_rfm.csv",index=False)

print(rfm.sort_values("Monetary",ascending=False).head(10))
print(rfm.sort_values("Frequency",ascending=False).head(10))
print(rfm.sort_values("Recency").head(10))
