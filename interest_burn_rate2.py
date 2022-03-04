# Add function to track expenses out in retirement years and net total decrease with compound interest

principal = 25000
interest = .32
numCompounds = 12
yearCounter = 0
growthYears = 4
contribution = 90000
retireYears = 35
retireIncome = 50000

# class testInterest:
# 	def __init__(self, interest, principal):
# 		self.interest = interest
# 		self.principal = principal
	
# def test():
# 	return testInterest()


def calcInterest(principal, interest, numCompounds, contribution):
	accrued = 0
	accrued = (principal * (1 + (interest / numCompounds)) ** numCompounds) - principal
	principal = principal * (1 + (interest / numCompounds)) ** numCompounds
	principal += contribution
	return principal, accrued

def calcInterestRetired(principal, interest, numCompounds, income):
	return principal - income * (1 + (interest / numCompounds)) ** numCompounds

while yearCounter < growthYears:
	yearCounter += 1
	principal, interestDelta = calcInterest(principal, interest, numCompounds, contribution)
	principal = round(principal, 2)
	interestDelta = round(interestDelta, 2)
	print(f'Year {yearCounter} Total: ${principal} | Interest: ${interestDelta}')

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