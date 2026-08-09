import pandas as pd
# Employee dataset
data = {
    "Name": ["John", "Sarah", "Mike", "Emma", "David", "Chris"],
    "Age": [25, 28, 27.33, 30, 27, 29],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT", "IT"],
    "Salary": [35000, 42000, 50000, 45000, 48000, 45000]
}
df = pd.DataFrame(data)
print("=" * 50)
print("           BUSINESS INSIGHTS REPORT")
print("=" * 50)
# Basic calculations
total_salary = df["Salary"].sum()
average_salary = df["Salary"].mean()
highest_salary = df["Salary"].max()
lowest_salary = df["Salary"].min()
total_employees = len(df)
highest_paid = df.loc[df["Salary"].idxmax(), "Name"]
lowest_paid = df.loc[df["Salary"].idxmin(), "Name"]
largest_department = df["Department"].value_counts().idxmax()
print("\nObservations:")
print(f"1. The company has {total_employees} employees.")
print(f"2. The total salary paid is ₹{total_salary:,}.")
print(f"3. The average employee salary is ₹{average_salary:,.2f}.")
print(f"4. {highest_paid} has the highest salary of ₹{highest_salary:,}.")
print(f"5. {lowest_paid} has the lowest salary of ₹{lowest_salary:,}.")
print(f"6. The {largest_department} department has the highest number of employees.")
print("\n" + "=" * 50)
print("           END OF REPORT")
print("=" * 50)