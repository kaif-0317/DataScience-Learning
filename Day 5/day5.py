import pandas as pd

df = pd.read_csv("employees.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Department"] = df["Department"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Display the updated dataset
print(df)