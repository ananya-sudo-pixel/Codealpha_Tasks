# 📊 Stock Portfolio Tracker – Python Project

Made by **Ananya** for **CodeAlpha Python Internship**

This project helps users manage a simple stock portfolio using Python.  
It has **two versions**:

- A **beginner version** where the user enters the price manually.
- An **advanced version** that fetches **live stock prices** from the internet using `yfinance`.

---

## 🗂 Project Structure

```text
CodeAlpha_StockPortfolio/
│
├── Stock_Portfolio.py          # Beginner version (manual price)
├── stock_portfolio_live.py     # Advanced version (live price)
├── README.md
└── screenshots/
    ├── basic/
    │   ├── menu_basic.png
    │   ├── add_stock_basic.png
    │   ├── view_basic.png
    │   └── total_basic.png
    └── live/
        ├── menu_live.png
        ├── fetch_price.png
        ├── view_live.png
        └── total_live.png
```

---

## 🚀 Features

🟢 Beginner Version – Stock_Portfolio.py

. Add a stock with:

    Name / symbol

    Quantity

    Price per share (entered manually)

.Calculates:

    Total value per stock → quantity × price

    Can display all stocks in a simple table format

. Shows total portfolio value.

## This version is offline and does not need internet.

## 🌐 Advanced Version – stock_portfolio_live.py

. Lets user enter:

    Stock symbol (e.g. TCS.NS, INFY.NS, AAPL)

    Quantity

. Uses yfinance to:

    Fetch the latest closing price from Yahoo Finance

    Handle invalid symbols / network errors safely

. Rounds:

    Price per share → 2 decimal places

    Total values → 2 decimal places

. If live price cannot be fetched, it falls back to manual price input.

This version is internet-based and needs both:

```bash
yfinance library

Active internet connection
```

---

## 📦 Technologies Used

| Component | Technology     |
| --------- | -------------- |
| Language  | Python 3       |
| Library   | `yfinance`     |
| Data      | Lists & dicts  |
| Interface | Terminal (CLI) |

---

## 🧩 How It Works (High Level)

## Beginner Version (Stock_Portfolio.py)

1. Shows a menu with options:

   Add a stock

   View portfolio

   Show total value

   Exit

2. Stores each stock as a dictionary:

```bash
{"name": name, "quantity": qty, "price": price}
```

3. Maintains a list of all stocks:

```bash
portfolio = []
```

4. Calculates totals by looping over the list.

---

## Advanced Version (stock_portfolio_live.py)

1. Uses yfinance.Ticker(symbol).history(period="1d") to get recent data.

2. Extracts the last closing price and uses it as the live price.

3. If fetching fails:

   Asks user to enter price manually.

4. Displays:

   Symbol

   Quantity

   Price (rounded)

   Total per stock

5. Sums up all totals to show total portfolio value.

---

## 🖥️ How to Run

🔹 Beginner Version

```bash
python Stock_Portfolio.py
```

🔹 Advanced (Live Price) Version

Install yfinance first (one time):

```bash
pip install yfinance
```

Then run:

```bash
python stock_portfolio_live.py
```

Make sure:

```bash
    Internet is ON

    Python 3 is installed
```

---

## 🖼️ Screenshots

    🟢 Beginner Version (Stock_Portfolio.py)

        ![Main Menu] (screenshots/basic/menu_basic.png)

        ![Add Stock] (screenshots/basic/add_stock_basic.png)

        ![View Portfolio] (screenshots/basic/view_basic.png)

        ![Total Portfolio Value] (screenshots/basic/total_basic.png)

    🌐 Advanced Live Version (stock_portfolio_live.py)

        ![Live Version Menu] (screenshots/live/menu_live.png)

        ![Fetching Live Price] (screenshots/live/fetch_price.png)

        ![Portfolio with Live Prices] (screenshots/live/view_live.png)

        ![Total Portfolio Value Live] (screenshots/live/total_live.png)

---

## 🏁 Project Info

Internship: CodeAlpha – Python Programming

Task: Stock Portfolio Tracker

## Developer: Pesala Ananya 💜
