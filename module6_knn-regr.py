import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = None

    def fit(self, x_values, y_values):
        """Initializes the data using a NumPy array."""
        # Storing as an (N, 2) array where column 0 is X and column 1 is Y
        self.points = np.column_stack((x_values, y_values))

    def predict(self, x_query):
        """Calculates k-NN Regression using Euclidean distance."""
        if self.points is None:
            return "Error: No data points provided."
        
        # 1. Calculate distances from x_query to all x points in the data
        # In 1D, Euclidean distance is just absolute difference
        distances = np.abs(self.points[:, 0] - x_query)
        
        # 2. Get the indices of the k smallest distances
        # argsort returns indices that would sort the array
        k_nearest_indices = np.argsort(distances)[:self.k]
        
        # 3. Retrieve the Y values for these k indices
        k_nearest_y = self.points[k_nearest_indices, 1]
        
        # 4. Return the mean of these Y values
        return np.mean(k_nearest_y)

def main():
    try:
        # Input N and k
        n = int(input("Enter the number of points (N): "))
        k = int(input("Enter the number of neighbors (k): "))

        if k > n:
            print(f"Error: k ({k}) cannot be greater than N ({n}).")
            return

        x_coords = []
        y_coords = []

        # Input N points
        for i in range(n):
            print(f"\nPoint {i+1}:")
            x = float(input("  Enter x value: "))
            y = float(input("  Enter y value: "))
            x_coords.append(x)
            y_coords.append(y)

        # Initialize and "fit" the model
        model = KNNRegressor(k)
        model.fit(np.array(x_coords), np.array(y_coords))

        # Final query
        x_test = float(input("\nEnter the X value to predict Y: "))
        result = model.predict(x_test)
        
        print(f"\nThe predicted Y value for X={x_test} is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
