# Armstrong Number Check

num = int(input("Enter a number: "))

# Convert number to string to get number of digits
power = len(str(num))

# Calculate sum of digits raised to the power
total = sum(int(digit) ** power for digit in str(num))

if num == total:
    print(f"{num} is an Armstrong number ✅")
else:
    print(f"{num} is NOT an Armstrong number ❌")
