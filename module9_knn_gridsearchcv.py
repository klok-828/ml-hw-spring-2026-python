import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from collections import Counter
import math
 
# --- Read Training Set ---
N = int(input("Enter N (number of training samples): "))
 
train_x = np.zeros(N)
train_y = np.zeros(N, dtype=int)
 
print("Enter training pairs (x then y) one by one:")
for i in range(N):
    train_x[i] = float(input(f"  Training sample {i+1} - x: "))
    train_y[i] = int(input(f"  Training sample {i+1} - y: "))
 
# Reshape X to 2D array as required by scikit-learn
X_train = train_x.reshape(-1, 1)
y_train = train_y
 
# --- Read Test Set ---
M = int(input("Enter M (number of test samples): "))
 
test_x = np.zeros(M)
test_y = np.zeros(M, dtype=int)
 
print("Enter test pairs (x then y) one by one:")
for i in range(M):
    test_x[i] = float(input(f"  Test sample {i+1} - x: "))
    test_y[i] = int(input(f"  Test sample {i+1} - y: "))
 
X_test = test_x.reshape(-1, 1)
y_test = test_y
 

min_class_count = min(Counter(y_train.tolist()).values())
 
if min_class_count >= 2:
    cv = min(5, min_class_count)
    # Each training fold has N - ceil(N/cv) samples; k must not exceed this
    min_fold_train_size = N - math.ceil(N / cv)
else:
    cv = LeaveOneOut()
    min_fold_train_size = N - 1  # LOO trains on N-1 each fold
 
max_k = min(10, min_fold_train_size) if min_fold_train_size > 0 else 1
param_grid = {"n_neighbors": list(range(1, max_k + 1))}
 

knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=cv, scoring="accuracy")
grid_search.fit(X_train, y_train)
 
best_k = grid_search.best_params_["n_neighbors"]
 
# Evaluate best model on test set
best_model = grid_search.best_estimator_
test_accuracy = best_model.score(X_test, y_test)
 
print(f"\nBest k: {best_k}")
print(f"Test Accuracy: {test_accuracy:.4f}")
