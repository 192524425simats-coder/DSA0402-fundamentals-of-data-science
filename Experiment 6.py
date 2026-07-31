prices = [100, 200, 150]
quantity = [2, 1, 3]

discount = 10
tax = 5

total = 0

for i in range(len(prices)):
    total = total + (prices[i] * quantity[i])

discount_amount = total * discount / 100
amount = total - discount_amount
tax_amount = amount * tax / 100
final_amount = amount + tax_amount

print("Total Price:", total)
print("Discount Amount:", discount_amount)
print("Tax Amount:", tax_amount)
print("Final Amount:", final_amount)
