import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
X = np.array([
    [2, 50],
    [3, 60],
    [4, 65],
    [5, 70],
    [6, 75],
    [7, 80],
    [8, 85],
    [9, 90]
])
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])
model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)
X_test = np.array([
    [3, 55],
    [5, 72],
    [8, 88],
    [4, 60]
])

y_test = np.array([0, 1, 1, 0])

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Actual Labels:")
print(y_test)
print("\nPredicted Labels:")
print(y_pred)
print("\nConfusion Matrix:")
print(cm)
print("\nAccuracy:")
print(accuracy)
print("\nError Rate:")
print(error_rate)
print("\nPrecision:")
print(precision)
print("\nRecall:")
print(recall)
print("\nF1-Score:")
print(f1)
