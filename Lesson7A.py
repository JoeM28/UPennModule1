# Import libraries
import pandas as pd
from sklearn import datasets, tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    cohen_kappa_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

# 1. Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2. Split into training and testing sets (60% train, 40% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

# 3. Train a Decision Tree Classifier
clf = tree.DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

# 4. Make predictions
y_pred = clf.predict(X_test)

# 5. Calculate metrics
acc = accuracy_score(y_test, y_pred)
kappa = cohen_kappa_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

# 6. Display results
print("=== Classification Metrics ===")
print(f"Accuracy: {acc:.2f}")
print(f"Cohen's Kappa: {kappa:.2f}")
print(f"Precision (macro): {precision:.2f}")
print(f"Recall (macro): {recall:.2f}")
print(f"F1 Score (macro): {f1:.2f}")

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(report)


# 1) Imports
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    explained_variance_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# 2) Load a regression dataset (Diabetes)
data = datasets.load_diabetes()
X = data.data          # features
y = data.target        # continuous target (disease progression)

# 3) Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

# 4) Fit Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# 5) Predict on the test set
y_pred = lr.predict(X_test)

# 6) Metrics
evs = explained_variance_score(y_test, y_pred)      # 1 - Var(y - ŷ) / Var(y)
mae = mean_absolute_error(y_test, y_pred)           # average |y - ŷ|
mse = mean_squared_error(y_test, y_pred)            # average (y - ŷ)^2
rmse = np.sqrt(mse)                                 # in target units
r2  = r2_score(y_test, y_pred)                      # 1 - SS_res / SS_tot

# 7) Display
print("=== Regression Metrics ===")
print(f"Explained Variance: {evs:.1f}")
print(f"Mean Absolute Error (MAE): {mae:.1f}")
print(f"Mean Squared Error (MSE): {mse:.1f}")
print(f"Root MSE (RMSE): {rmse:.1f}")
print(f"R^2 Score: {r2:.1f}")


from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import metrics

# Load data
X, y = datasets.load_iris(return_X_y=True)

# Fit KMeans model
kmeans = KMeans(n_clusters=3, random_state=43)
labels_pred = kmeans.fit_predict(X)

# True labels (for evaluation only)
labels_true = y

# === Clustering Evaluation Metrics ===
ari = metrics.adjusted_rand_score(labels_true, labels_pred)
mi = metrics.adjusted_mutual_info_score(labels_true, labels_pred)
homogeneity = metrics.homogeneity_score(labels_true, labels_pred)
completeness = metrics.completeness_score(labels_true, labels_pred)
v_measure = metrics.v_measure_score(labels_true, labels_pred)
silhouette = metrics.silhouette_score(X, labels_pred)

print("=== Clustering Metrics ===")
print(f"Adjusted Rand Index: {ari:.3f}")
print(f"Adjusted Mutual Info: {mi:.3f}")
print(f"Homogeneity: {homogeneity:.3f}")
print(f"Completeness: {completeness:.3f}")
print(f"V-Measure: {v_measure:.3f}")
print(f"Silhouette Coefficient: {silhouette:.3f}")

print("Predicted cluster labels:", labels_pred)


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

X, y = datasets.load_iris(return_X_y=True)

kmeans = KMeans(n_clusters=3, random_state=43)
labels_pred = kmeans.fit_predict(X)

plt.figure(figsize=(10, 4))

# Actual classes
plt.subplot(1, 2, 1)
plt.scatter(X[:, 2], X[:, 3], c=y, cmap='viridis')
plt.title("Actual Iris Species (True Labels)")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

# KMeans predicted clusters
plt.subplot(1, 2, 2)
plt.scatter(X[:, 2], X[:, 3], c=labels_pred, cmap='viridis')
plt.title("K-Means Predicted Clusters")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

plt.show()
