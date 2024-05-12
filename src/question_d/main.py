def create_multiplication_table():
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print("\t".join(map(str, row)))

def main():
    while True:
        table = create_multiplication_table()
        print("Multiplication Table:")
        display_multiplication_table(table)
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != "yes":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()