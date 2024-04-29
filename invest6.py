import random

principal = 125000
interest_rate = .065
comps_yearly = 12
growth_time = 25

def calc_interest(principal, int_rate, comps_yearly, time):
	amount = principal * (1 + int_rate / comps_yearly) ** (comps_yearly * time)
	return amount

for years in range(growth_time):
	principal = calc_interest(principal, interest_rate, comps_yearly, growth_time)
	print(principal)


