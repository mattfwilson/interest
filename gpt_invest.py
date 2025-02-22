import pandas as pd

initial_portfolio = 1200000
withdrawal_rate = 0.04
inflation = 0.03
investment_return = 0.06
years = 30

years_list = []
portfolio_list = []
withdrawal_list = []

portfolio_value = initial_portfolio
withdrawal_amount = initial_portfolio * withdrawal_rate

for year in range(1, years + 1):
    years_list.append(year)
    portfolio_list.append(portfolio_value)
    withdrawal_list.append(withdrawal_amount)
    
    # Withdraw the adjusted amount
    portfolio_value -= withdrawal_amount
    
    # Apply investment return
    portfolio_value *= (1 + investment_return)
    
    # Adjust next year's withdrawal for inflation
    withdrawal_amount *= (1 + inflation)

df = pd.DataFrame({
    "Year": years_list,
    "Portfolio Value ($)": portfolio_list,
    "Withdrawal ($)": withdrawal_list
})

df.head(25)
print(df.head(25))

