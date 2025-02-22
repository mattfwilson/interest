import numpy as np
import matplotlib.pyplot as plt

def early_retirement_calculator(principal, withdrawal, inflation, return_rate, tax_rate, penalty_rate, retirement_age, ss_age, ss_benefit, ss_growth, current_age=39):
    balance = principal
    annual_withdrawal = withdrawal
    ss_annual_benefit = ss_benefit
    balances = []
    ages = []
    
    age = current_age
    while age <= 100:  # Ensure calculations until age 100
        ages.append(age)
        balances.append(balance)
        
        # Determine actual withdrawal needed from investments
        if age >= ss_age:
            withdrawal_needed = max(0, annual_withdrawal - ss_annual_benefit)
            ss_annual_benefit *= (1 + ss_growth)  # Adjust Social Security for COLA
        else:
            withdrawal_needed = annual_withdrawal
        
        # Apply taxes and penalties if withdrawing before standard retirement age
        if age < retirement_age:
            withdrawal_needed *= (1 + penalty_rate)
        withdrawal_needed *= (1 + tax_rate)
        
        # Withdraw from investments
        balance -= withdrawal_needed
        
        # Grow remaining balance
        if balance > 0:
            balance *= (1 + return_rate)
        else:
            break
        
        # Adjust withdrawal for inflation
        annual_withdrawal *= (1 + inflation)
        
        age += 1
    
    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(ages, balances, label="Investment Balance", color="blue")
    plt.axhline(y=0, color="red", linestyle="--", label="Depletion Point")
    plt.xlabel("Age")
    plt.ylabel("Investment Balance ($)")
    plt.title("Early Retirement Balance Over Time")
    plt.legend()
    plt.grid()
    plt.show()
    
    return ages[-1] if balance <= 0 else "Funds last until age 100 or beyond"

# Example Usage
early_retirement_calculator(
    principal=1_350_000, 
    withdrawal=43_000, 
    inflation=0.03, 
    return_rate=0.06, 
    tax_rate=0.21, 
    penalty_rate=0.10, 
    retirement_age=44, 
    ss_age=67, 
    ss_benefit=30_000, 
    ss_growth=0.02
)

