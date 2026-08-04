import pandas as pd

# Create Dataset
data = {
    "Name": ["John", "Sarah", "Mike", "Emma", "David"],
    "Age": [25, 28, 27, 30, 26],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT"],
    "Salary": [35000, 42000, 50000, 45000, 48000]
}
df = pd.DataFrame(data)

# Display Dataset
print("Employee Dataset")
print(df)

# Data Analysis
total_salary = df["Salary"].sum()
average_salary = df["Salary"].mean()
minimum_salary = df["Salary"].min()
maximum_salary = df["Salary"].max()
employee_count = df["Name"].count()
print("\n" + "=" * 40)
print("      EMPLOYEE DATA ANALYSIS REPORT")
print("=" * 40)
print(f"Total Employees      : {employee_count}")
print(f"Total Salary Paid    : ₹{total_salary:,}")
print(f"Average Salary       : ₹{average_salary:,.2f}")
print(f"Highest Salary       : ₹{maximum_salary:,}")
print(f"Lowest Salary        : ₹{minimum_salary:,}")
print("\nBusiness Insights")
print("-" * 40)
highest_paid = df.loc[df["Salary"].idxmax(), "Name"]
lowest_paid = df.loc[df["Salary"].idxmin(), "Name"]
print(f"• Highest paid employee : {highest_paid}")
print(f"• Lowest paid employee  : {lowest_paid}")
print("\nAnalysis Completed Successfully!")
print("=" * 40)