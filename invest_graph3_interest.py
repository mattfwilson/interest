principal = 1000
int_rate = .075
comp_years = 20
int_accrued = []

def calc_interest(principal, rate, time):
    amount = 0
    for year in range(time):
        amount = principal * rate * time
        int_accrued.append(amount)
    return amount

calc_interest(principal, int_rate, comp_years)

for amount in int_accrued:
    print(amount)