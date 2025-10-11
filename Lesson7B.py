# ==== Imports ====
import numpy as np
from collections import Counter
from sklearn import datasets, tree
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -------------------------------------------------------
# Part A: IRIS — Decision Tree (classification)
# -------------------------------------------------------
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target
species_names = iris.target_names  # ['setosa','versicolor','virginica']

# Train / test split (not strictly needed for a quick demo, but good practice)
Xi_tr, Xi_te, yi_tr, yi_te = train_test_split(X_iris, y_iris, test_size=0.3, random_state=0)

dt = tree.DecisionTreeClassifier(random_state=0)
dt.fit(Xi_tr, yi_tr)

# ---- Predict for a sample flower (sepal len, sepal wid, petal len, petal wid)
sample_iris1 = np.array([[5.1, 3.5, 1.4, 0.2]])  # you can change this
print("Single Sample iris features:", sample_iris1)
dt_pred_idx = dt.predict(sample_iris1)[0]
print("DT prediction idx:", dt_pred_idx)
dt_pred_name = species_names[dt_pred_idx]
print("Decision Tree → Predicted species:", dt_pred_name)

#Predict 5 samples Decision Tree classifier
# ---- Predict for 5 sample flowers ----
# Each inner list = [sepal length, sepal width, petal length, petal width]
sample_iris5 = np.array([
    [5.1, 3.5, 1.4, 0.2],  # likely setosa
    [6.7, 3.0, 5.2, 2.3],  # likely virginica
    [5.9, 3.0, 4.2, 1.5],  # likely versicolor
    [4.9, 3.1, 1.5, 0.1],  # likely setosa
    [6.0, 2.7, 5.1, 1.6]   # likely virginica
])
print("\n 5 Sample iris features:", sample_iris5)

# Predict class indices for all 5
dt_pred_indices = dt.predict(sample_iris5)
print("Raw predicted indices:", dt_pred_indices)  # e.g. [0 2 1 0 2]

# Convert numeric indices (0/1/2) to species names
dt_pred_names = [species_names[i] for i in dt_pred_indices]
print("Predicted species names:", dt_pred_names)



# -------------------------------------------------------
# Part B: IRIS — KMeans (clustering)
# -------------------------------------------------------
# Fit KMeans on the **features only** (unsupervised)
kmeans = KMeans(n_clusters=3, n_init='auto', random_state=43)
kmeans.fit(X_iris)

# Raw KMeans cluster prediction (0/1/2)
km_cluster = kmeans.predict(sample_iris1)[0]
print("KMeans → Predicted cluster ID:", km_cluster)

# OPTIONAL: map clusters to real species names by majority vote (post-hoc labeling)
# (This is just to make clusters human-readable; KMeans itself does not know species.)
cluster_labels = kmeans.labels_  # cluster assignment for every training point
mapping = {}  # cluster_id -> majority species name
for c in range(3):
    true_labels_in_c = y_iris[cluster_labels == c]
    if len(true_labels_in_c) == 0:
        mapping[c] = "unknown"
    else:
        majority_idx = Counter(true_labels_in_c).most_common(1)[0][0]
        mapping[c] = species_names[majority_idx]

print("KMeans → Cluster-to-species mapping (by majority vote):", mapping)
print("KMeans → Interpreted as species:", mapping[km_cluster])

print("KMeans for 5 samples")
# Predict cluster IDs for each sample

sample_iris5 = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [6.7, 3.0, 5.2, 2.3],
    [5.9, 3.0, 4.2, 1.5],
    [4.9, 3.1, 1.5, 0.1],
    [6.0, 2.7, 5.1, 1.6]
])

# Predict clusters
km_clusters = kmeans.predict(sample_iris5)
print("KMeans → Predicted cluster IDs:", km_clusters)

# Build mapping safely
mapping = {}
for c in range(kmeans.n_clusters):
    true_labels_in_c = y_iris[np.array(kmeans.labels_) == c]
    if len(true_labels_in_c) == 0:
        mapping[int(c)] = "unknown"
    else:
        majority_idx = Counter(true_labels_in_c).most_common(1)[0][0]
        mapping[int(c)] = str(species_names[majority_idx])

print("KMeans → Cluster-to-species mapping (by majority vote):", mapping)

# Predict species names
km_species = [mapping[int(c)] for c in km_clusters]
print("KMeans → Interpreted species predictions:", km_species)


# -------------------------------------------------------
# Part C: DIABETES — Linear Regression (regression)
# -------------------------------------------------------
# Load the regression dataset (10 standardized features, continuous target)
diab = datasets.load_diabetes()
X_dia, y_dia = diab.data, diab.target

Xd_tr, Xd_te, yd_tr, yd_te = train_test_split(X_dia, y_dia, test_size=0.3, random_state=0)

lr = LinearRegression()
lr.fit(Xd_tr, yd_tr)

# For a quick demo, use one real sample from the test set (you can replace with your own 10-feature vector)
sample_diabetes = Xd_te[0].reshape(1, -1)
dia_pred = lr.predict(sample_diabetes)[0]

print("Linear Regression (Diabetes) → Predicted target value:", round(dia_pred, 2))

# If you want to predict with your own diabetes sample:
# Provide a 10-element array in the same scaled feature space as X_dia (since dataset is standardized).
# custom_diabetes = np.array([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]])
# print("Custom Diabetes prediction:", lr.predict(custom_diabetes)[0])
