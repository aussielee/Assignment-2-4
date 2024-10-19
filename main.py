# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = salary * 0.065  # Calculate state withholding tax at 6.5%
federalTax = salary * 0.28  # Calculate federal withholding tax at 28.0%
dependentDeduction = salary * 0.025 * numDependents  # Calculate dependent deductions
totalWithholding = stateTax + federalTax + dependentDeduction  # Total withholding
takeHomePay = salary - totalWithholding  # Calculate take-home pay

# output statements

# Print state tax with 2 decimal places
print(f"State Tax: ${stateTax:.2f}")

# Print federal tax with 2 decimal places
print(f"Federal Tax: ${federalTax:.2f}")

# Print dependent deduction with 2 decimal places
print(f"Dependents: ${dependentDeduction:.2f}")

# Print original salary
print("Salary: $" + str(salary))

# Print take-home pay after deductions
print("Take Home Pay: $" + str(takeHomePay))
