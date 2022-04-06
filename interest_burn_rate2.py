# Add function to track expenses out in retirement years and net total decrease with compound interest

principal = 660000
interest = .0725
numCompounds = 12
yearCounter = 0
growthYears = 10
contribution = 36000
retireYears = 40
retirement = 0
retireIncome = 30000

class Summary:
	def __init__(self, principal, interest, retireYears):
		self.principal = principal
		self.interest = interest
		self.retireYears = retireYears
	
	def displaySummary(self):
		dollars = "${:,.2f}".format(self.principal)
		percentage = "{:.2%}".format(self.interest)
		annualTotal = round(self.principal / self.retireYears, 2)
		monthlyTotal = round(annualTotal / 12, 2)
		print(f"\nTotal before withdrawing: {dollars}")
		print(f"Interest rate: {percentage}")
		print(f"Annual retire spend: ${annualTotal}")
		print(f"Monthly retire spend: ${monthlyTotal}\n")

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

stats = Summary(principal, interest, retireYears)
stats.displaySummary()

while retirement < retireYears:
	principal = principal - retireIncome
	principal = calcInterestRetired(principal, interest, numCompounds, retireIncome)
	principal = round(principal, 2)
	retireYears -= 1
	print(f'Retired Year {retireYears}: ${principal}')
	if principal <= 0:
		print(f'You\'re out of money! Go get that bread again...')
		break