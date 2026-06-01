import numpy as np
from sklearn.metrics import precision_score, recall_score
 
# Read N
while True:
    try:
        N = int(input("Enter the number of points (positive integer): "))
        if N > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
 
# Initialize arrays using NumPy
X = np.zeros(N, dtype=int)  # ground truth labels
Y = np.zeros(N, dtype=int)  # predicted labels
 
# Read N (x, y) points
for i in range(N):
    print(f"\nPoint {i + 1}:")
    while True:
        try:
            x = int(input("  Enter x (ground truth, 0 or 1): "))
            if x in (0, 1):
                break
            print("  x must be 0 or 1.")
        except ValueError:
            print("  Invalid input. Please enter 0 or 1.")
    while True:
        try:
            y = int(input("  Enter y (predicted,   0 or 1): "))
            if y in (0, 1):
                break
            print("  y must be 0 or 1.")
        except ValueError:
            print("  Invalid input. Please enter 0 or 1.")
    X[i] = x
    Y[i] = y
 
# Compute Precision and Recall using scikit-learn
precision = precision_score(X, Y, zero_division=0)
recall    = recall_score(X, Y, zero_division=0)
 
print("\n--- Results ---")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
