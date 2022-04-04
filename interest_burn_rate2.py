# Add function to track expenses out in retirement years and net total decrease with compound interest

principal = 660000
interest = .0725
numCompounds = 12
yearCounter = 0
growthYears = 10
contribution = 36000
retireYears = 40
retireIncome = 50000

class Summary:
	def __init__(self, principal, interest):
		self.principal = principal
		self.interest = interest
	
	def displayPrincipal(self):
		dollars = "${:,.2f}".format(self.principal)
		print(f"Your principal amount is: {dollars}")

	def displayInterest(self):
		percentage = "{:.2%}".format(self.interest)
		print(f"Your interest rate is: {percentage}")


def calcInterest(principal, interest, numCompounds, contribution):
	accrued = (principal * (1 + (interest / numCompounds)) ** numCompounds) - principal
	principal = principal + accrued
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

annualTotal = round(principal / retireYears, 2)
monthlyTotal = round(annualTotal / 12, 2)

print(f'\nAnnual spend total: ${annualTotal}')
print(f'Monthly spend total: ${monthlyTotal}\n')

stats = Summary(principal, interest)
stats.displayPrincipal()
stats.displayInterest()

# while retireYears > 0:
# 	principal = principal - retireIncome
# 	principal = calcInterestRetired(principal, interest, numCompounds, retireIncome)
# 	principal = round(principal, 2)
# 	retireYears -= 1
# 	print(f'Retired Year {retireYears}: ${principal}')
# 	if principal <= 0:
# 		print('You\'re out of money!')
# 		break