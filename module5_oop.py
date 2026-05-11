

class NumberCollection:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def find_number(self, x):
        for index in range(len(self.numbers)):
            if self.numbers[index] == x:
                return index + 1  
        return -1


def main():
    N = int(input("Enter a positive integer N: "))

    collection = NumberCollection()

    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        collection.insert_number(num)

    X = int(input("Enter integer X to search: "))

    result = collection.find_number(X)
    print(result)


if __name__ == "__main__":
    main()
