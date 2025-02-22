import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import random

def early_retirement_calculator(principal, withdrawal, withdrawal_alt, inflation, return_rate, retirement_age, ss_age, ss_benefit, ss_growth, tax_brackets, recession_impact=0.20, recession_years=[], recession_duration=1, current_age=39, pre_retirement_return=0.07, monthly_contribution=1500):
    balance = principal
    balance_tax_optimized = principal
    balance_no_ss = principal
    balance_alt = principal
    annual_withdrawal = withdrawal
    annual_withdrawal_alt = withdrawal_alt
    ss_annual_benefit = ss_benefit
    balances = []
    balances_tax_optimized = []
    balances_no_ss = []
    balances_alt = []
    ages = []
    
    age = current_age
    while age < retirement_age:
        ages.append(age)
        balances.append(balance)
        balances_tax_optimized.append(balance_tax_optimized)
        balances_no_ss.append(balance_no_ss)
        balances_alt.append(balance_alt)
        
        # Grow balance at a higher rate until retirement age
        balance *= (1 + pre_retirement_return)
        balance_tax_optimized *= (1 + pre_retirement_return)
        balance_no_ss *= (1 + pre_retirement_return)
        balance_alt *= (1 + pre_retirement_return)
        
        # Add monthly contributions
        balance += monthly_contribution * 12
        balance_tax_optimized += monthly_contribution * 12
        balance_no_ss += monthly_contribution * 12
        balance_alt += monthly_contribution * 12
        
        age += 1
    
    while age <= 100:
        ages.append(age)
        balances.append(balance)
        balances_tax_optimized.append(balance_tax_optimized)
        balances_no_ss.append(balance_no_ss)
        balances_alt.append(balance_alt)
        
        # Determine actual withdrawal needed from investments
        if age >= ss_age:
            ss_annual_benefit *= (1 + ss_growth)  # Adjust Social Security for COLA
            withdrawal_needed = max(0, annual_withdrawal - ss_annual_benefit)
            withdrawal_needed_alt = max(0, annual_withdrawal_alt - ss_annual_benefit)
            balance += ss_annual_benefit  # Include SS in standard balance
            balance_alt += ss_annual_benefit
        else:
            withdrawal_needed = annual_withdrawal
            withdrawal_needed_alt = annual_withdrawal_alt
        
        withdrawal_needed_no_ss = annual_withdrawal  # No Social Security scenario
        
        # Withdraw from investments
        balance -= withdrawal_needed
        balance_no_ss -= withdrawal_needed_no_ss
        balance_alt -= withdrawal_needed_alt
        
        # Tax-optimized withdrawal strategy
        taxable_withdrawal = min(withdrawal_needed, tax_brackets[0])  # Withdraw at the lowest tax bracket
        remaining_withdrawal = max(0, withdrawal_needed - taxable_withdrawal)
        
        if remaining_withdrawal > 0:
            taxable_withdrawal += remaining_withdrawal * (1 + tax_brackets[1])
        
        balance_tax_optimized -= taxable_withdrawal
        
        # Grow remaining balance with recessions applied
        if any(age - current_age >= year and age - current_age < year + recession_duration for year in recession_years):
            balance *= (1 - recession_impact)
            balance_tax_optimized *= (1 - recession_impact)
            balance_no_ss *= (1 - recession_impact)
            balance_alt *= (1 - recession_impact)
        
        if balance > 0:
            balance *= (1 + return_rate)
        if balance_tax_optimized > 0:
            balance_tax_optimized *= (1 + return_rate)
        if balance_no_ss > 0:
            balance_no_ss *= (1 + return_rate)
        if balance_alt > 0:
            balance_alt *= (1 + return_rate)
        else:
            break
        
        # Adjust withdrawal for inflation
        annual_withdrawal *= (1 + inflation)
        annual_withdrawal_alt *= (1 + inflation)
        
        age += 1
    
    # Plot results
    plt.figure(figsize=(20, 10))
    plt.plot(ages, balances, label="$45,000/yr Withdrawal Rate", color="blue", linewidth=2)
    plt.plot(ages, balances_alt, label="$55,000/yr Withdrawal Rate", color="purple", linestyle="-.", linewidth=2)
    plt.plot(ages, balances_tax_optimized, label="Tax-Optimized Balance", color="green", linestyle="--", linewidth=2)
    plt.plot(ages, balances_no_ss, label="No Social Security Balance", color="orange", linestyle=":", linewidth=2)
    plt.axhline(y=0, color="red", linestyle="--", linewidth=2, label="Balance Depletion Point")
    plt.xlabel("Age")
    plt.ylabel("Investment Balance ($)")
    plt.title("Early Retirement Balance Over Time (All Lines Assume Recessions/SS/Optimizing Taxliability)")
    plt.legend(title='Balance Amounts', loc='upper left')
    plt.grid()
    
    # Format y-axis to show full dollar amounts
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))
    
    plt.get_current_fig_manager().window.title("Retirement Calculator")
    
    plt.show()
    
    return "Retirement balance calculations completed"

rand_rec = []

for i in range(3):
    rand_year = random.randint(10, 40)
    rand_rec.append(rand_year)

# Example Usage
early_retirement_calculator(
    principal=1_150_000, 
    withdrawal=45_000, 
    withdrawal_alt=55_000, 
    inflation=0.03, 
    return_rate=0.06, 
    retirement_age=45, 
    ss_age=67, 
    ss_benefit=30_000, 
    ss_growth=0.02, 
    tax_brackets=[0.10, 0.22],  # Example tax brackets
    recession_impact=0.20,  # 20% drop due to recession
    recession_years=rand_rec,  # Recessions occur at years 10, 20, and 30
    recession_duration=1,  # Each recession lasts 1 year
    pre_retirement_return=0.06,  # 6% compound growth until retirement age
    monthly_contribution=1500  # Monthly investments until retirement
)


