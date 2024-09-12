income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected savings after one year, with interest
interest_rate = 0.05
annual_savings = monthly_savings * 12
savings = annual_savings * (1 + interest_rate)

print(f"Projected savings after one year, with interest, is: ${savings:.2f}")
