# Add function to track expenses out in retirement years and net total decrease with compound interest
# Add functionality to separate interest gained over a year from total principal + contribution + interest

principal = 600000
interest = .065
numCompounds = 12
yearCounter = 0
growthYears = 18
contribution = 30000
output = []
retireYears = 35
retireIncome = 40000

def calcInterest(principal, interest, numCompounds, contribution):
	principal += contribution
	return principal * (1 + (interest / numCompounds)) ** numCompounds

def calcInterestRetired(principal, interest, numCompounds, income):
	return principal - income * (1 + (interest / numCompounds)) ** numCompounds

while yearCounter < growthYears:
	yearCounter += 1
	principal = calcInterest(principal, interest, numCompounds, contribution)
	principal = round(principal, 2)
	print(f"Growth Year {yearCounter}: ${principal}")

annualTotal = principal / retireYears
monthlyTotal = annualTotal / 12

print(f'\nAnnual total: ${annualTotal}')
print(f'Monthly total: ${monthlyTotal}\n')

while retireYears > 0:
	principal = principal - retireIncome
	principal = calcInterestRetired(principal, interest, numCompounds, retireIncome)
	principal = round(principal, 2)
	retireYears -= 1
	print(f'Retired Year {retireYears}: ${principal}')
	if principal <= 0:
		print('You\'re out of money!')
		break