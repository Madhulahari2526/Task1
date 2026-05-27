# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 150,
    "MSFT": 320
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Number of stocks user wants to add
n = int(input("How many stocks do you want to enter? "))

# Store portfolio details
portfolio = []

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    # Check if stock exists
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio.append([stock_name, quantity, investment])

        print(f"Added {stock_name} - Investment Value: ${investment}")

    else:
        print("❌ Stock not found!")

# Display portfolio summary
print("\n📊 Portfolio Summary")
for stock in portfolio:
    print(f"Stock: {stock[0]}, Quantity: {stock[1]}, Value: ${stock[2]}")

print("\n💰 Total Investment Value: $", total_investment)

# Optional: Save results to a text file
save = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-------------------------\n")

        for stock in portfolio:
            file.write(f"Stock: {stock[0]}, Quantity: {stock[1]}, Value: ${stock[2]}\n")

        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("✅ Portfolio saved to portfolio.txt")