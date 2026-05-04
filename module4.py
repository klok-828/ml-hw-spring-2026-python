# Ask for N
N = int(input("Enter a positive integer N: "))

numbers = []

# Read N numbers one by one
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask for X
X = int(input("Enter X: "))

# Check if X exists in the list
if X in numbers:
    # index() returns 0-based index, so add 1
    print(numbers.index(X) + 1)
else:
    print(-1)
