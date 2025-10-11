import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
#print(iris)
print(iris.feature_names)
print(iris.target_names)
x,y=iris.data, iris.target
print(x.shape)
print(y.shape)
print(x[:2])
print(y[:2]) #First two samples are of same flower type

#Train Test Split
print("\nTrain Test Split")
print("x is features, y is labels")
from sklearn.model_selection import train_test_split, cross_validate

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.4, random_state=0)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)
print(x_train[:2])
print(y_train[:2])
print(x_test[:2])
print(y_test[:2])
print("Training samples:", x_train.shape[0])
print("Testing samples:", x_test.shape[0])
print("\nFirst training example:")
print("x_train:", x_train[0])
print("y_train:", y_train[0])

#Import Tree model
from sklearn import tree
model = tree.DecisionTreeClassifier().fit(x_train, y_train)
print("model score")
print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

#Cross Validation
print("\nCross Validation")
from sklearn.model_selection import cross_val_score
clf2 = tree.DecisionTreeClassifier()
scores = cross_val_score(clf2, x_train, y_train, cv=5)
print("Cross Validation scores/Accuracies :", scores)
print("Mean CV accuracy :", scores.mean())
print("Standard Deviation of CV accuracy :", scores.std())
print("Max CV accuracy :", scores.max())
print("Min CV accuracy :", scores.min())
print("Number of CV scores :", scores.shape[0])
print("All CV scores :", scores)
print("First CV score :", scores[0])
print("Last CV score :", scores[-1])
print(pd.Series(scores).describe())

#Cross Validation

from sklearn.model_selection import cross_val_score
scoring=['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
scores = cross_validate(clf2, x_train, y_train, scoring=scoring ,cv= 5, return_train_score=False)
pd.set_option('display.expand_frame_repr', False)
print("\nCross Validation with multiple metrics")
print(pd.DataFrame(scores))
print(pd.DataFrame(scores).describe())
scores_df =pd.DataFrame(scores).round(2)
print("\nCV scores ROUNDED")
print(scores_df)
print("\nMean CV scores with multiple metrics")
print(scores_df.mean().round(2))
print("\nStandard Deviation of CV scores with multiple metrics")
print(scores_df.std().round(2))
print("\nMax CV scores with multiple metrics")
print(scores_df.max().round(2))
print("\nMin CV scores with multiple metrics")
print(scores_df.min().round(2))
print("\nFirst CV scores with multiple metrics")
print(scores_df.iloc[0])
print("\nLast CV scores with multiple metrics")
print(scores_df.iloc[-1])

