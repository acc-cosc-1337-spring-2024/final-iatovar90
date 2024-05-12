class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def main():
    # Create instances of Stock class for each stock
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]

    # Display the symbol and company name for each stock
    print("Stock Report:")
    print("Company\t\tSymbol")
    for stock in stocks:
        print(f"{stock.get_company_name()}\t{stock.get_symbol()}")

if __name__ == "__main__":
    main()