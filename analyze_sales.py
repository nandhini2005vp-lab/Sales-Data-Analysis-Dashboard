import pandas as pd
df = pd.read_csv("sales_data.csv")
print(df)
print("Total Sales:",df["Sales"].sum())

print(df.groupby("Product") ["Sales"].sum())

print(df.groupby("Region") ["Sales"].sum())