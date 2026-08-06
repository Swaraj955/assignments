import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(len(df))
print((df["FinalResult"] == 1).sum())
print((df["FinalResult"] == 0).sum())