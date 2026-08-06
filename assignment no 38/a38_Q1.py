import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# First 5 records
print("First 5 Records:")
print(df.head())

# Last 5 records
print("\nLast 5 Records:")
print(df.tail())

# Total rows and columns
print("\nShape:", df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)