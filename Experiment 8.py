import pandas as pd

data = {
    "Product": ["Pen", "Book", "Pen", "Pencil", "Book", "Eraser", "Pen", "Scale"],
    "Quantity": [10, 15, 20, 8, 12, 5, 18, 9]
}

sales_data = pd.DataFrame(data)

top5 = sales_data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print("Top 5 Products Sold:")
print(top5)
