#This program calculates the total price of items in a list. It first prints the sum of the prices and then calculates the total using a loop, displaying the final total at the end.$¢
prices = [10, 20, 30]
for item in (prices):
    print(sum(prices))
    break

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")