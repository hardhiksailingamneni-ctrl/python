n = int(input("Number of products: "))
budget = float(input("Budget: "))

total = 0

for i in range(n):
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    total += price * qty

if total > 5000:
    total = total * 0.9

print("Final Amount =", total)

if total > budget:
    print("Over Budget by", total - budget)
else:
    print("Within Budget")