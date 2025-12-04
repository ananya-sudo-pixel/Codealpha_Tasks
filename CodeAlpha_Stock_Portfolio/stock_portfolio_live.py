# Stock Portfolio Tracker - Live Price Version (Advanced)
# Uses internet to fetch live stock prices using yfinance.
# Made by Anu for CodeAlpha Python Internship

import yfinance as yf

# This list will store all the stocks the user adds.
# Each stock will be a dictionary with: symbol, quantity, price.
portfolio = []


def show_menu():
    """Display the main menu options."""
    print("\nStock Portfolio Tracker (Live Prices)")
    print("1. Add a stock (with live price)")
    print("2. View portfolio")
    print("3. Show total portfolio value")
    print("4. Exit")


def fetch_live_price(symbol):
    """
    Fetch the latest closing price for a stock symbol using yfinance.
    Returns the price as a float, or None if it fails.
    """
    try:
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="1d")

        if history.empty:
            return None

        # Get the last closing price
        price = float(history["Close"].iloc[-1])
        return price
    except Exception:
        return None


def add_stock_live():
    """Add a new stock to the portfolio using a live price from the internet."""
    print("\nAdd a new stock (live price)")

    symbol = input("Enter stock symbol (e.g. TCS.NS, INFY.NS, AAPL): ").strip().upper()
    quantity_input = input("Enter quantity (number of shares): ").strip()

    # Convert quantity to a number safely
    try:
        quantity = int(quantity_input)
    except ValueError:
        print("Invalid quantity. Stock not added.")
        return

    print("Fetching live price for", symbol, "...")

    price = fetch_live_price(symbol)

    if price is None:
        print("Could not fetch live price for this symbol.")
        manual_price_input = input("Enter price per share manually: ").strip()

        try:
            price = float(manual_price_input)
        except ValueError:
            print("Invalid price. Stock not added.")
            return
    else:
        print("Live price fetched successfully! Price per share:", price)

    stock = {
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
    }

    portfolio.append(stock)
    print("Stock added successfully!")


def view_portfolio():
    """Display all the stocks in the portfolio."""
    print("\nYour Portfolio:")

    if not portfolio:
        print("No stocks added yet.")
        return

    # Table header
    print(f"{'No.':<5}{'Symbol':<12}{'Qty':<10}{'Price':<15}{'Total':<15}")

    # Table rows
    for index, stock in enumerate(portfolio, start=1):
        symbol = stock["symbol"]
        quantity = stock["quantity"]
        price = round(stock["price"], 2)
        total = round(quantity * price, 2)


        print(f"{index:<5}{symbol:<12}{quantity:<10}{price:<15}{total:<15}")


def show_total_value():
    """Calculate and display the total value of the portfolio."""
    if not portfolio:
        print("\nNo stocks in portfolio yet.")
        return

    total_value = 0

    for stock in portfolio:
        quantity = stock["quantity"]
        price = stock["price"]
        total_value += quantity * price
    total_value = round(total_value, 2)
    print("\nTotal portfolio value:", total_value)


def main():
    """Main loop to run the menu and handle user choices."""
    print("Note: This version uses live prices. Please make sure you have internet and 'yfinance' installed.")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_stock_live()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            show_total_value()
        elif choice == "4":
            print("Thank you for using the Stock Portfolio Tracker (Live Prices).")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
