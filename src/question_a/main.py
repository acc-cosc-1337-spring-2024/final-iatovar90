def main():
    # Initialize an empty list to store the numbers
    numbers = []

    # Ask the user to enter 5 numbers
    for i in range(5):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)

    # Calculate the lowest number
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num

    # Calculate the highest number
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num

    # Calculate the total of the numbers
    total = sum(numbers)

    # Calculate the average of the numbers
    average = total / len(numbers)

    # Display the results
    print(f"The lowest number is: {lowest}")
    print(f"The highest number is: {highest}")
    print(f"The total of the numbers is: {total}")
    print(f"The average of the numbers is: {average}")

if __name__ == "__main__":
    main()