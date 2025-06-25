import matplotlib.pyplot as plt

principal = 1_150_000
low_rate = 0.054
high_rate = 0.092
years = 30

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

	plt.figure(figsize=(16, 10))
	plt.plot(years_lst, c_bal_low, label='Low Rate {}%'.format(round(low_rate * 100), 3), color="red", linestyle='--', linewidth=2)
	plt.plot(years_lst, c_bal_high, label='High Rate {}%'.format(round(high_rate * 100), 3), color="green", linestyle='--', linewidth=2)

	plt.xlabel('Time (Years)')
	plt.ylabel('Balance ($ in millions)')
	plt.title('Investment Growth Over Time')
	plt.legend()
	plt.grid()
	plt.show()

	return c_bal_low[-1], c_bal_high[-1]


totals = compound(principal, low_rate, high_rate, years)
print(f'Low: {convert_dollars(totals[0])}\nHigh: {convert_dollars(totals[1])}')
