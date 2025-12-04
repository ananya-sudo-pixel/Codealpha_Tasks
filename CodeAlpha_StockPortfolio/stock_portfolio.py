# Stock Portfolio Tracker - Beginner Version
# Made by Anu for CodeAlpha Python Internship

# This list will store all the stocks the user adds.
# Each stock will be a dictionary with: name, quantity, price.
portfolio = []


def show_menu():
    """Display the main menu options."""
    print("\nStock Portfolio Tracker")
    print("1. Add a stock")
    print("2. View portfolio")
    print("3. Show total portfolio value")
    print("4. Exit")


def add_stock():
    """Add a new stock to the portfolio."""
    print("\nAdd a new stock")

    name = input("Enter stock name (e.g. TCS, INFY): ").strip()
    quantity_input = input("Enter quantity (number of shares): ").strip()
    price_input = input("Enter price per share: ").strip()

    # Convert quantity and price to numbers safely
    try:
        quantity = int(quantity_input)
        price = float(price_input)
    except ValueError:
        print("Invalid number entered. Stock not added.")
        return

    stock = {
        "name": name,
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
    print(f"{'No.':<5}{'Name':<12}{'Qty':<10}{'Price':<12}{'Total':<12}")

    # Table rows
    for index, stock in enumerate(portfolio, start=1):
        name = stock["name"]
        quantity = stock["quantity"]
        price = stock["price"]
        total = quantity * price

        print(f"{index:<5}{name:<12}{quantity:<10}{price:<12}{total:<12}")


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

    print("\nTotal portfolio value:", total_value)


def main():
    """Main loop to run the menu and handle user choices."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            show_total_value()
        elif choice == "4":
            print("Thank you for using the Stock Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
