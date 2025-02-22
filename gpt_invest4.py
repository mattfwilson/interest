import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(principal, withdrawal, inflation, mean_return, std_dev, tax_rate, penalty_rate, retirement_age, ss_age, ss_benefit, ss_growth, current_age=39, num_simulations=1000):
    np.random.seed(42)  # For reproducibility
    simulations = []
    
    for _ in range(num_simulations):
        balance = principal
        annual_withdrawal = withdrawal
        ss_annual_benefit = ss_benefit
        balances = []
        ages = []
        age = current_age
        
        while age <= 100:
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
            
            # Grow remaining balance with random market return
            if balance > 0:
                random_return = np.random.normal(mean_return, std_dev)
                balance *= (1 + random_return)
            else:
                break
            
            # Adjust withdrawal for inflation
            annual_withdrawal *= (1 + inflation)
            
            age += 1
        
        simulations.append(balances)
    
    # Plot results
    plt.figure(figsize=(10, 5))
    for sim in simulations[:100]:  # Plot only 100 simulations for clarity
        plt.plot(range(current_age, current_age + len(sim)), sim, color='blue', alpha=0.1)
    
    plt.axhline(y=0, color="red", linestyle="--", label="Depletion Point")
    plt.xlabel("Age")
    plt.ylabel("Investment Balance ($)")
    plt.title("Monte Carlo Simulations of Early Retirement Balance Over Time")
    plt.legend()
    plt.grid()
    plt.show()
    
    return "Monte Carlo simulations completed"

# Example Usage
monte_carlo_simulation(
    principal=1_150_000, 
    withdrawal=45_000, 
    inflation=0.025, 
    mean_return=0.06, 
    std_dev=0.15,  # Market volatility assumption
    tax_rate=0.15, 
    penalty_rate=0.10, 
    retirement_age=45, 
    ss_age=67, 
    ss_benefit=30_000, 
    ss_growth=0.02
)

