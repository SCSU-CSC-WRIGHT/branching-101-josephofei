"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""


def run():
    total = 0

    for i in range(5):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is:", total)


def main():
    run()  # Call the function that contains your code


if __name__ == "__main__":
    main()
