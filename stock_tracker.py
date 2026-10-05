prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 330}

portfolio = {}
total = 0

print("Available stocks:", ", ".join(prices))

while True:
    name = input("\nStock name (or 'done'): ").upper()
    if name == "DONE":
        break
    if name not in prices:
        print("Stock not found!")
        continue
    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("Enter a valid number.")
        continue
    value = prices[name] * qty
    portfolio[name] = portfolio.get(name, 0) + qty
    total += value
    print(f"{name}: {qty} x {prices[name]} = {value}")

print("\n--- Portfolio ---")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares = {prices[stock] * qty}")
print("Total investment:", total)

with open("portfolio.txt", "w") as f:
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares = {prices[stock] * qty}\n")
    f.write(f"Total investment: {total}\n")