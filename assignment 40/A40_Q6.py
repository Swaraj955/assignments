import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

result = X_test.copy()
result["Actual"] = y_test.values
result["Predicted"] = y_pred

misclassified = result[result["Actual"] != result["Predicted"]]

print(misclassified)
print("Misclassified Count:", len(misclassified))