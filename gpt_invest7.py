import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import random


def on_key(event):
    """Close the figure when the Esc key is pressed."""
    if event.key == 'escape':
        plt.close(event.canvas.figure)

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
        
        balance *= (1 + pre_retirement_return)
        balance_tax_optimized *= (1 + pre_retirement_return)
        balance_no_ss *= (1 + pre_retirement_return)
        balance_alt *= (1 + pre_retirement_return)
        
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
        
        if age >= ss_age:
            ss_annual_benefit *= (1 + ss_growth)
            withdrawal_needed = max(0, annual_withdrawal - ss_annual_benefit)
            withdrawal_needed_alt = max(0, annual_withdrawal_alt - ss_annual_benefit)
            balance += ss_annual_benefit
            balance_alt += ss_annual_benefit
        else:
            withdrawal_needed = annual_withdrawal
            withdrawal_needed_alt = annual_withdrawal_alt
        
        withdrawal_needed_no_ss = annual_withdrawal
        
        balance -= withdrawal_needed
        balance_no_ss -= withdrawal_needed_no_ss
        balance_alt -= withdrawal_needed_alt
        
        taxable_withdrawal = min(withdrawal_needed, tax_brackets[0])
        remaining_withdrawal = max(0, withdrawal_needed - taxable_withdrawal)
        
        if remaining_withdrawal > 0:
            taxable_withdrawal += remaining_withdrawal * (1 + tax_brackets[1])
        
        balance_tax_optimized -= taxable_withdrawal
        
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
        
        annual_withdrawal *= (1 + inflation)
        annual_withdrawal_alt *= (1 + inflation)
        
        age += 1
    
    global fig
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(ages, balances, label="$45,000/yr Withdrawal Rate", color="blue", linewidth=2)
    ax.plot(ages, balances_alt, label="$55,000/yr Withdrawal Rate", color="purple", linestyle="-.", linewidth=2)
    ax.plot(ages, balances_tax_optimized, label="Tax-Optimized Balance", color="green", linestyle="--", linewidth=2)
    ax.plot(ages, balances_no_ss, label="No Social Security Balance", color="orange", linestyle=":", linewidth=2)
    ax.axhline(y=0, color="red", linestyle="--", linewidth=2, label="Balance Depletion Point")
    ax.set_xlabel("Age")
    ax.set_ylabel("Investment Balance ($)")
    ax.set_title("Early Retirement Balance Over Time (All Lines Assume Recessions/SS/Optimizing Tax Liability)")
    ax.legend(title='Balance Amounts', loc='upper left')
    ax.grid()
    ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))
    fig.canvas.mpl_connect('key_press_event', on_key)

    plt.show()
    
rand_rec = [random.randint(10, 40) for _ in range(3)]

early_retirement_calculator(
    principal=1_100_000, 
    withdrawal=45_000, 
    withdrawal_alt=55_000, 
    inflation=0.03, 
    return_rate=0.07, 
    retirement_age=43, 
    ss_age=70, 
    ss_benefit=30_000, 
    ss_growth=0.02, 
    tax_brackets=[0.10, 0.22], 
    recession_impact=0.25, 
    recession_years=rand_rec, 
    recession_duration=1, 
    pre_retirement_return=0.06, 
    monthly_contribution=2000
)

