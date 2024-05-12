class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stock_list = {
        "AAPL": Stock("AAPL", "Apple Inc"),
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google"),
        "MSFT": Stock("MSFT", "Microsoft")
    }

    print("Stock Purchase History:")
    for symbol, stock in stock_list.items():
        print(f"Symbol: {stock.get_symbol()}, Company Name: {stock.get_company_name()}")

def main():
    while True:
        print("\nMenu:")
        print("1- Display stock purchase history")
        print("2- Exit")
        option = input("Select an option: ")

        if option == "1":
            stock_purchase_history()
        elif option == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main()