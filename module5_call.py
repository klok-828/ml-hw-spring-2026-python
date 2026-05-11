from module5_mod import NumberCollection


def main():
    # Read N
    N = int(input("Enter a positive integer N: "))

    collection = NumberCollection()

    # Read N numbers
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        collection.insert_number(num)

    # Read X
    X = int(input("Enter integer X to search: "))

    # Search and print result
    result = collection.find_number(X)
    print(result)


if __name__ == "__main__":
    main()
