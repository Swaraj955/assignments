import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(df["StudyHours"].mean())
print(df["Attendance"].mean())
print(df["PreviousScore"].max())
print(df["SleepHours"].min())