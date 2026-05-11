class NumberCollection:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def find_number(self, x):
        for index in range(len(self.numbers)):
            if self.numbers[index] == x:
                return index + 1   # 1-based index
        return -1
