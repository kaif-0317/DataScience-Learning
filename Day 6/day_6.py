import pandas as pd

data = {
    "Name": ["John", "Sarah", "Mike", "Emma", "David", "Chris"],
    "Age": [25, 28, 22, 30, 27, 29],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT", "HR"],
    "Salary": [35000, 42000, 50000, 45000, 48000, 40000]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

print("\nEmployees with Salary > 40000")
print(df[df["Salary"] > 40000])

print("\nEmployees in IT Department")
print(df[df["Department"] == "IT"])

print("\nEmployees in IT Department with Salary > 45000")
print(df[(df["Department"] == "IT") & (df["Salary"] > 45000)])

print("\nSelected Columns (Name and Department)")
print(df[["Name", "Department"]])

print("\nSorted by Salary (Ascending)")
print(df.sort_values(by="Salary"))

print("\nSorted by Salary (Descending)")
print(df.sort_values(by="Salary", ascending=False))

print("\nSorted by Name")
print(df.sort_values(by="Name"))