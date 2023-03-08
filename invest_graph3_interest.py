principal = 1000
int_rate = .075
comp_years = 20
int_accrued = []

def calc_interest(P, r, t):
    A = 0
    for year in range(t):
        A = P * r * t
        int_accrued.append(A)
    return A

calc_interest(principal, int_rate, comp_years)

for amount in int_accrued:
    print(amount)