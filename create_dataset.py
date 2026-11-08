import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor",
                "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics",
                 "Electronics", "Accessories", "Accessories", "Electronics",
                 "Electronics", "Accessories"],
    "Quantity": [2, 5, 3, 1, 2, 4, 6, 1, 3, 7],
    "Price": [50000, 500, 1500, 50000, 12000, 500, 1500, 12000, 50000, 500],
    "Region": ["Chennai", "Chengalpattu", "Chennai", "Madurai", "Chennai",
               "Madurai", "Chengalpattu", "Chennai", "Madurai", "Chennai"]
}

df = pd.DataFrame(data)

df["Sales"] = df["Quantity"] * df["Price"]

df.to_csv("sales_data.csv", index=False)

print("Sales dataset created successfully!")
print(df)