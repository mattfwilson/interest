# Add function to track expenses out in retirement years and net total decrease with compound interest
# Add functionality to separate interest gained over a year from total principal + contribution + interest
# Test @mattfwilson git account

principal = 650000
interest = .065
numCompounds = 12
yearCounter = 0
growthYears = 15
contribution = 12000
retireYears = 35
retireIncome = 50000

class testInterest:
	def __init__(self, interest, principal):
		self.interest = interest
		self.principal = principal
	
def test():
	return testInterest()


def calcInterest(principal, interest, numCompounds, contribution):
	accrued = 0
	accrued -= (principal * (1 + (interest / numCompounds)) ** numCompounds) - principal
	principal = principal * (1 + (interest / numCompounds)) ** numCompounds
	principal += contribution
	print(accrued)
	return principal

def calcInterestRetired(principal, interest, numCompounds, income):
	return principal - income * (1 + (interest / numCompounds)) ** numCompounds

while yearCounter < growthYears:
	yearCounter += 1
	principal = calcInterest(principal, interest, numCompounds, contribution)
	principal = round(principal, 2)
	print(f"Growth Year {yearCounter}: ${principal} | Interest: ")

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