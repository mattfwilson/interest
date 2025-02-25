import matplotlib.pyplot as plt

principal = 1_150_000
low_rate = 0.06
high_rate = 0.10
years = 10

def convert_dollars(amount):
	return f"${amount:,.2f}"

def compound(principal, low_rate, high_rate, years):
	low_bal = principal
	high_bal = principal
	low_int_rate = low_rate
	high_int_rate = high_rate
	c_years = years
	years_lst = list(range(1, years + 1))
	c_bal_low = []
	c_bal_high = []

	while c_years > 0:
		low_bal *= round((1 + low_int_rate), 2)
		c_bal_low.append(low_bal)
		high_bal *= round((1 + high_int_rate), 2)
		c_bal_high.append(high_bal)
		c_years -= 1

	print(f"{low_int_rate:.1%} Rate Final Balance:", convert_dollars(c_bal_low[-1]))
	print(f"{high_int_rate:.1%} Rate Final Balance:", convert_dollars(c_bal_high[-1]))

	plt.figure(figsize=(16, 10))
	plt.plot(years_lst, c_bal_low, label="Low Rate", color="red", linestyle="--", linewidth=2)
	plt.plot(years_lst, c_bal_high, label="High Rate", color="blue", linestyle="--", linewidth=2)

	plt.xlabel("Time (Years)")
	plt.ylabel("Balance ($)")
	plt.title("Investment Growth Over Time")
	plt.legend()
	plt.grid()
	plt.show()

compound(principal, low_rate, high_rate, years)

