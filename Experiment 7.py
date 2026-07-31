import pandas as pd

data = {
    "Customer_ID": [101, 102, 101, 103, 102],
    "Order_Date": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-08", "2024-01-20"],
    "Product_Name": ["Pen", "Book", "Pen", "Pencil", "Book"],
    "Order_Quantity": [5, 10, 8, 6, 12]
}

order_data = pd.DataFrame(data)

print("Total Orders by Each Customer:")
print(order_data["Customer_ID"].value_counts())

print("\nAverage Order Quantity for Each Product:")
print(order_data.groupby("Product_Name")["Order_Quantity"].mean())

print("\nEarliest Order Date:")
print(order_data["Order_Date"].min())

print("\nLatest Order Date:")
print(order_data["Order_Date"].max())
