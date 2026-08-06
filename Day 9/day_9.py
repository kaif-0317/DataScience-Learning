import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
data = {
    "Name": ["John", "Sarah", "Mike", "Emma", "David"],
    "Age": [25, 28, 27, 30, 26],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT"],
    "Salary": [35000, 42000, 50000, 45000, 48000]
}
df = pd.DataFrame(data)
df
total_salary = df["Salary"].sum()
average_salary = df["Salary"].mean()
maximum_salary = df["Salary"].max()
minimum_salary = df["Salary"].min()
employee_count = df["Name"].count()
print("========== EMPLOYEE DASHBOARD ==========")
print(f"Total Employees : {employee_count}")
print(f"Total Salary    : ₹{total_salary}")
print(f"Average Salary  : ₹{average_salary:.2f}")
print(f"Highest Salary  : ₹{maximum_salary}")
print(f"Lowest Salary   : ₹{minimum_salary}")
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()
department_counts = df["Department"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    department_counts,
    labels=department_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Employees by Department")
plt.show()
plt.figure(figsize=(6,4))
plt.plot(df["Name"], df["Salary"], marker="o")
plt.title("Salary Trend")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()