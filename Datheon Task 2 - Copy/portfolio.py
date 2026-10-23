
import csv
import os
from datetime import datetime

# Sample stock prices for demonstration.
# These are example prices, NOT live market prices.
market_prices = {
    "TCS": 3500.00,
    "INFY": 1500.00,
    "RELIANCE": 1400.00,
    "WIPRO": 500.00,
    "HDFCBANK": 1700.00
}

portfolio = {}

print("=" * 45)
print("INVESTMENT PORTFOLIO TRACKER")
print("=" * 45)

while True:
    ticker = input("\nEnter stock ticker (or DONE to finish): ").strip().upper()

    if ticker == "DONE":
        break

    if not ticker:
        print("Please enter a valid ticker.")
        continue

    try:
        buy_price = float(input("Enter buy price per share (₹): "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            continue

        if ticker in market_prices:
            current_price = market_prices[ticker]
        else:
            current_price = float(
                input("Enter example current price per share (₹): ")
            )
            if current_price <= 0:
                print("Current price must be positive.")
                continue

        if ticker in portfolio:
            old = portfolio[ticker]
            old_quantity = old["quantity"]
            total_quantity = old_quantity + quantity

            old["buy_price"] = (
                old["buy_price"] * old_quantity
                + buy_price * quantity
            ) / total_quantity

            old["quantity"] = total_quantity
            old["current_price"] = current_price
        else:
            portfolio[ticker] = {
                "buy_price": buy_price,
                "quantity": quantity,
                "current_price": current_price
            }

        print(f"{ticker} added successfully!")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if not portfolio:
    print("\nNo stocks were entered. Exiting.")
    raise SystemExit

total_invested = 0
total_market_value = 0
total_profit_loss = 0

print("\n" + "=" * 90)
print(f"{'STOCK':<12}{'QTY':>6}{'BUY PRICE':>14}"
      f"{'CURRENT':>14}{'INVESTED':>15}{'VALUE':>15}{'GAIN/LOSS %':>14}")
print("=" * 90)

rows = []

for ticker, stock in portfolio.items():
    buy_price = stock["buy_price"]
    quantity = stock["quantity"]
    current_price = stock["current_price"]

    invested = buy_price * quantity
    market_value = current_price * quantity
    profit_loss = market_value - invested
    percentage = (profit_loss / invested) * 100

    total_invested += invested
    total_market_value += market_value
    total_profit_loss += profit_loss

    print(
        f"{ticker:<12}{quantity:>6}{buy_price:>14.2f}"
        f"{current_price:>14.2f}{invested:>15.2f}"
        f"{market_value:>15.2f}{percentage:>13.2f}%"
    )

    rows.append({
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Ticker": ticker,
        "Quantity": quantity,
        "Average Buy Price": round(buy_price, 2),
        "Current Price (Example)": round(current_price, 2),
        "Invested Capital": round(invested, 2),
        "Market Value": round(market_value, 2),
        "Profit/Loss": round(profit_loss, 2),
        "Gain/Loss Percentage": round(percentage, 2)
    })

overall_percentage = (
    total_profit_loss / total_invested
) * 100

print("=" * 90)
print(f"Total Invested:     ₹{total_invested:.2f}")
print(f"Current Value:      ₹{total_market_value:.2f}")
print(f"Total Profit/Loss:  ₹{total_profit_loss:.2f}")
print(f"Overall Return:      {overall_percentage:.2f}%")
print("=" * 90)

filename = "portfolio_summary.csv"
file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())

    if not file_exists:
        writer.writeheader()

    writer.writerows(rows)

print(f"\nReport saved successfully to: {filename}")
