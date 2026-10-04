print("=" * 40)
print(" function treat ")
print("=" * 40)





def stats(data):
    """Calculate basic statistics."""
    return len(data), sum(data), min(data), max(data), sum(data)/len(data)


def multiple(*args):
    """Display multiple values using *args."""
    for x in args:
        print(x)


def show_summary(**kwargs):
    """Display dataset summary using **kwargs."""
    for k, v in kwargs.items():
        print(f"{k}: {v}")


def factorial(n):
    """Calculate factorial using recursion."""
    return 1 if n <= 1 else n * factorial(n - 1)


def analyze(data):
    """Analyze the dataset."""
    global summary

    n, total, minimum, maximum, average = stats(data)
    summary = {"Count": n, "Sum": total, "Average": average}

    print("\n--- Statistics ---")
    print("Count:", n)
    print("Sum:", total)
    print("Min:", minimum)
    print("Max:", maximum)
    print("Average:", average)


def main():
    """Main menu of Data Analyzer."""

    data = list(map(int, input(
        "Enter numbers separated by space: ").split()))

    while True:
        print("\n===== DATA ANALYZER =====")
        print("1. Statistics")
        print("2. Sort")
        print("3. Filter")
        print("4. Factorial")
        print("5. *args / **kwargs")
        print("6. 2D List")
        print("7. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            analyze(data)

        elif ch == "2":
            print("Ascending:", sorted(data))
            print("Descending:", sorted(data, reverse=True))

        elif ch == "3":
            limit = int(input("Enter limit: "))
            print("Filtered:",
                  list(filter(lambda x: x > limit, data)))

        elif ch == "4":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif ch == "5":
            multiple(10, 20, 30)
            show_summary(**summary)

        elif ch == "6":
            rows = int(input("Rows: "))
            matrix = []
            for i in range(rows):
                matrix.append(list(map(int, input(
                    f"Row {i+1}: ").split())))

            print("2D List:")
            for row in matrix:
                print(*row)

        elif ch == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()