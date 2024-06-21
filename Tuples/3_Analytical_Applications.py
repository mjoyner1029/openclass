stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def calculate_average_closing_price(stock_data, stock_symbol, start_date):
    total = 0
    count = 0

    for data in stock_data:
        symbol, date, closing_price = data
        if symbol == stock_symbol and date >= start_date:
            total += closing_price
            count += 1

    if count == 0:
        return "No data found for the specified stock symbol and start date."

    average_closing_price = total / count
    return average_closing_price

# Test the function
stock_symbol = "AAPL"
start_date = "2021-01-01"
average_price = calculate_average_closing_price(stock_data, stock_symbol, start_date)
print(f"The average closing price for {stock_symbol} from {start_date} onwards is: {average_price}")

