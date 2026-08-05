import matplotlib.pyplot as plt

# Sample Data
departments = ["HR", "Finance", "IT", "Marketing"]
employees = [10, 15, 25, 12]
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 25000, 30000, 28000, 35000]
expense_labels = ["Rent", "Salary", "Utilities", "Others"]
expenses = [30, 45, 15, 10]
# ----------------------------
# BAR CHART
# ----------------------------
plt.figure(figsize=(6,4))
plt.bar(departments, employees)
plt.title("Employees in Each Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()
# ----------------------------
# LINE CHART
# ----------------------------
plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)
plt.show()
# ----------------------------
# PIE CHART
# ----------------------------
plt.figure(figsize=(6,6))
plt.pie(expenses,
        labels=expense_labels,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Company Expenses Distribution")
plt.show()