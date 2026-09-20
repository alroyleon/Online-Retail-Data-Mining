import pandas as pd
df = pd.read_excel("D:/data_mining/data/raw/online_retail_II.xlsx")

pd.set_option("display.max_columns", None)
print(df[df["Price"] < 0])
print("---------------------")

print(df["Invoice"].astype(str).str.startswith("C").sum())
print("---------------------")

print(df[df["Invoice"].astype(str).str.startswith("C")]["Invoice"].nunique())
print("---------------------")

print((
    (df["Quantity"] < 0) &
    (df["Invoice"].astype(str).str.startswith("C"))
).sum())
print("---------------------")

print((
    (df["Quantity"] < 0) &
    (~df["Invoice"].astype(str).str.startswith("C"))
).sum())
print("---------------------")

print(df[
    (df["Quantity"] < 0) &
    (~df["Invoice"].astype(str).str.startswith("C"))
].head(20))
print("---------------------")
print(df[
    (df["Quantity"] < 0) &
    (~df["Invoice"].astype(str).str.startswith("C"))
]["Description"].value_counts().head(20))

