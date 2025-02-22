import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def early_retirement_calculator(principal, withdrawal, inflation, return_rate, retirement_age, ss_age, ss_benefit, ss_growth, tax_brackets, current_age=39):
    balance = principal
    balance_tax_optimized = principal
    balance_no_ss = principal
    annual_withdrawal = withdrawal
    ss_annual_benefit = ss_benefit
    balances = []
    balances_tax_optimized = []
    balances_no_ss = []
    ages = []
    
    age = current_age
    while age <= 100:
        ages.append(age)
        balances.append(balance)
        balances_tax_optimized.append(balance_tax_optimized)
        balances_no_ss.append(balance_no_ss)
        
        # Determine actual withdrawal needed from investments
        if age >= ss_age:
            withdrawal_needed = max(0, annual_withdrawal - ss_annual_benefit)
            ss_annual_benefit *= (1 + ss_growth)  # Adjust Social Security for COLA
        else:
            withdrawal_needed = annual_withdrawal
        
        withdrawal_needed_no_ss = annual_withdrawal  # No Social Security scenario
        
        # Withdraw from investments
        balance -= withdrawal_needed
        balance_no_ss -= withdrawal_needed_no_ss
        
        # Tax-optimized withdrawal strategy
        taxable_withdrawal = min(withdrawal_needed, tax_brackets[0])  # Withdraw at the lowest tax bracket
        remaining_withdrawal = max(0, withdrawal_needed - taxable_withdrawal)
        
        if remaining_withdrawal > 0:
            taxable_withdrawal += remaining_withdrawal * (1 + tax_brackets[1])
        
        balance_tax_optimized -= taxable_withdrawal
        
        # Grow remaining balance
        if balance > 0:
            balance *= (1 + return_rate)
        if balance_tax_optimized > 0:
            balance_tax_optimized *= (1 + return_rate)
        if balance_no_ss > 0:
            balance_no_ss *= (1 + return_rate)
        else:
            break
        
        # Adjust withdrawal for inflation
        annual_withdrawal *= (1 + inflation)
        
        age += 1
    
    # Plot results
    plt.figure(figsize=(20, 10))
    plt.plot(ages, balances, label="Standard Investment Balance", color="blue", linewidth=2)
    plt.plot(ages, balances_tax_optimized, label="Tax-Optimized Balance", color="green", linestyle="--", linewidth=2)
    plt.plot(ages, balances_no_ss, label="No Social Security Balance", color="orange", linestyle=":", linewidth=2)
    plt.axhline(y=0, color="red", linestyle="--", linewidth=2, label="Depletion Point")
    plt.xlabel("Age")
    plt.ylabel("Investment Balance ($)")
    plt.title("Early Retirement Balance Over Time (Standard, Tax-Optimized, No SS)")
    plt.legend()
    plt.grid()
    
    # Format y-axis to show full dollar amounts
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))
    
    plt.get_current_fig_manager().window.title("Retirement Calculator")
    
    plt.show()
    
    return "Retirement balance calculations completed"

# Example Usage
early_retirement_calculator(
    principal=1_150_000, 
    withdrawal=45_000, 
    inflation=0.025, 
    return_rate=0.06, 
    retirement_age=45, 
    ss_age=67, 
    ss_benefit=30_000, 
    ss_growth=0.02, 
    tax_brackets=[0.10, 0.22]  # Example tax brackets
)
