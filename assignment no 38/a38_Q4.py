import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

count = df["FinalResult"].value_counts()
print(count)

percentage = df["FinalResult"].value_counts(normalize=True) * 100
print(percentage)

if abs(percentage[1] - percentage[0]) < 10:
    print("Dataset is balanced.")
else:
    print("Dataset is not balanced.")