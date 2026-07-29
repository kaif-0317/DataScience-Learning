# Add Two Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)



# Check Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    

# Find Factorial

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)


# Multiplication Table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
    
    
# Largest of Three Numbers

