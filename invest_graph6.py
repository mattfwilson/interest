import matplotlib.pyplot as plt

principal = 1_150_000
low_return_rate = 0.06
high_return_rate = 0.10
years = 20

def convert_dollars(amount):
	return f"${amount:,.2f}"

def compound(principal, low_rate, high_rate, years):
	low_balance = principal
	high_balance = principal
	low_int_rate = low_rate
	high_int_rate = high_rate
	c_years = years
	years_lst = list(range(1, years + 1))
	c_balance_low = []
	c_balance_high = []

	while c_years > 0:
		low_balance *= round((1 + low_int_rate), 2)
		c_balance_low.append(low_balance)
		high_balance *= round((1 + high_int_rate), 2)
		c_balance_high.append(high_balance)
		c_years -= 1

	print(f"{low_int_rate:.1%} Rate Final Balance:", convert_dollars(c_balance_low[-1]))
	print(f"{high_int_rate:.1%} Rate Final Balance:", convert_dollars(c_balance_high[-1]))

	plt.figure(figsize=(16, 10))
	plt.plot(years_lst, c_balance_low, label="Low Rate", color="red", linestyle="--", linewidth=2)
	plt.plot(years_lst, c_balance_high, label="High Rate", color="blue", linestyle="--", linewidth=2)

	plt.xlabel("Time (Years)")
	plt.ylabel("Balance ($)")
	plt.title("Investment Growth Over Time")
	plt.legend()
	plt.grid()
	plt.show()

compound(principal, low_return_rate, high_return_rate, years)

