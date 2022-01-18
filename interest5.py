# Add function to track expenses out in retirement years and net total decrease with compound interest

principal = 635000
interest = .07
numCompounds = 12
yearCounter = 0
growthYears = 15
contribution = 30000
output = []
retireYears = 40
retireIncome = 75000

def calcInterest(principal, interest, numCompounds, contribution):
	principal += contribution
	return principal * (1 + (interest / numCompounds)) ** numCompounds

def calcInterestRetired(principal, interest, numCompounds):
	return principal * (1 + (interest / numCompounds)) ** numCompounds

while yearCounter < growthYears:
	yearCounter += 1
	principal = calcInterest(principal, interest, numCompounds, contribution)
	principal = round(principal, 2)
	print(f"Year {yearCounter}: ${principal}")

annualTotal = principal / retireYears
monthlyTotal = annualTotal / 12

print(f'\nAnnual total: ${annualTotal}')
print(f'Monthly total: ${monthlyTotal}\n')

while retireYears > 0:
	principal = principal - retireIncome
	principal = calcInterestRetired(principal, interest, numCompounds)
	principal = round(principal, 2)
	retireYears -= 1
	print(f'{retireYears} Total: ${principal}')
	if principal <= 0:
		print('You\'re out of money!')
		break