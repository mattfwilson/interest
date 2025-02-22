import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Constants
initial_principal = 750000  # Initial investment
sp500_return = 0.10  # 10% S&P 500 average return
inflation_rate = 0.025  # 2.5% inflation
withdrawal_rates = [0.03, 0.04, 0.05]  # 3%, 4%, and 5% withdrawal rates
retirement_ages = [15, 20, 25]  # Withdrawals start after these years
years = 40

# Create figure
plt.figure(figsize=(12, 6))

# Compute and plot each scenario
for retirement_age in retirement_ages:
    for withdrawal_rate in withdrawal_rates:
        years_list = np.arange(0, years + 1)
        nominal_values = np.zeros(years + 1)
        nominal_values[0] = initial_principal
        initial_withdrawal = withdrawal_rate * initial_principal  # First-year withdrawal

        for year in range(1, years + 1):
            if year < retirement_age:
                nominal_values[year] = nominal_values[year - 1] * (1 + sp500_return)
            else:
                withdrawal_amount = initial_withdrawal * ((1 + inflation_rate) ** (year - retirement_age))
                nominal_values[year] = nominal_values[year - 1] * (1 + sp500_return) - withdrawal_amount

        # Plot the portfolio growth
        label = f"Retire {retirement_age}yr, {int(withdrawal_rate * 100)}% WD"
        plt.plot(years_list, nominal_values, label=label)

# Compute and plot Principal Growth (No Withdrawals)
principal_growth = initial_principal * (1 + sp500_return) ** years_list
plt.plot(years_list, principal_growth, label="No Withdrawals", linestyle="dashed", color="black")

# Labels and Title
plt.xlabel("Years")
plt.ylabel("Portfolio Value ($)")
plt.title("Portfolio Growth with Different Retirement Ages & Withdrawal Rates")
plt.legend()
plt.grid(True)

# Format y-axis to show full dollar amounts
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))

# Show plot
plt.show()

