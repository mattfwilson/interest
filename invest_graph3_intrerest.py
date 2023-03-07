principal = 675000
int_rate = .075
comp_years = 13
contribution = 22500
int_accrued = []

for year in range(comp_years):
    total = principal * int_rate
    int_accrued.append(total)
print(int_accrued)
