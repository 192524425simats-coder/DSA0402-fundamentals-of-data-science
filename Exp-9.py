import pandas as pd

data = {
    "Property_ID": [101, 102, 103, 104],
    "Location": ["Chennai", "Chennai", "Hyderabad", "Bangalore"],
    "Bedrooms": [3, 5, 4, 6],
    "Area": [1200, 1800, 1500, 2200],
    "Price": [5000000, 8000000, 6500000, 9000000]
}

property_data = pd.DataFrame(data)

print("Average Listing Price:")
print(property_data.groupby("Location")["Price"].mean())

print("\nProperties with More than 4 Bedrooms:")
print((property_data["Bedrooms"] > 4).sum())

print("\nProperty with Largest Area:")
print(property_data.loc[property_data["Area"].idxmax()])

