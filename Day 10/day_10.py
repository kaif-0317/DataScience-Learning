import pandas as pd

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\KAIF\OneDrive\Desktop\codomax\Day 10\cleaned_employee_data.csv")
print("Cleaned Dataset")
print(df)

# Export the cleaned dataset
df.to_csv(r"C:\Users\KAIF\OneDrive\Desktop\codomax\Day 10\exported_employee_data.csv", index=False)
print("\nCleaned dataset exported successfully!")
print("File name: exported_employee_data.csv")