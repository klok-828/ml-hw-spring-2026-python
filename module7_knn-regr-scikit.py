import numpy as np
from sklearn.neighbors import KNeighborsRegressor
 
def main():
    # --- Read N ---
    while True:
        try:
            N = int(input("Enter N (number of training points, positive integer): "))
            if N > 0:
                break
            print("N must be a positive integer. Try again.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
 
    # --- Read k ---
    while True:
        try:
            k = int(input("Enter k (number of neighbors, positive integer): "))
            if k > 0:
                break
            print("k must be a positive integer. Try again.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
 
    # --- Read N (x, y) points using NumPy ---
    points = np.zeros((N, 2))  # Initialize N×2 array with NumPy
 
    print(f"\nEnter {N} training point(s). Provide x then y for each point.")
    for i in range(N):
        while True:
            try:
                x_val = float(input(f"  Point {i + 1} — x: "))
                y_val = float(input(f"  Point {i + 1} — y: "))
                points[i] = [x_val, y_val]   # NumPy row insertion
                break
            except ValueError:
                print("  Invalid input. x and y must be real numbers. Try again.")
 
    # Separate features and labels using NumPy slicing
    X_train = points[:, 0].reshape(-1, 1)  # Shape (N, 1)
    y_train = points[:, 1]                 # Shape (N,)
 
    # --- Variance of labels in the training dataset ---
    label_variance = np.var(y_train)
    print(f"\nVariance of labels (y) in training dataset: {label_variance:.6f}")
 
    # --- Validate k <= N ---
    if k > N:
        print(f"\nError: k ({k}) must be less than or equal to N ({N}). "
              f"Cannot perform {k}-NN regression with only {N} training point(s).")
        return
 
    # --- Read query X ---
    while True:
        try:
            X_query = float(input("\nEnter X (query point for prediction): "))
            break
        except ValueError:
            print("Invalid input. X must be a real number.")
 
    # --- k-NN Regression using Scikit-learn ---
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)
 
    X_pred = np.array([[X_query]])          # NumPy array for prediction input
    Y_pred = model.predict(X_pred)[0]
 
    print(f"\n--- Result ---")
    print(f"k-NN Regression (k={k}) prediction at X = {X_query}: Y = {Y_pred:.6f}")
 
if __name__ == "__main__":
    main()
