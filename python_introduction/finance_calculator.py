monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}")

# Calculate projected savings after one year, with interest
interest_rate = 0.05
annual_savings = monthly_savings * 12
savings = annual_savings * (1 + interest_rate)

print(f"Projected savings after one year, with interest, is: ${savings:.2f}")