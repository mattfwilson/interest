principal = 100000
compInterest = .05
contributionGrowth = .015
contribution = 12000
start = 0
growthYears = 20

def calcInterest(totalSavings, interest, annualContribution):
	return annualContribution + totalSavings * (1 + interest)

while start < growthYears:
	start += 1
	contribution *= (1 + contributionGrowth)
	principal = calcInterest(principal, compInterest, contribution)
	principal = round(principal, 2)
	print(f"Year {start}: ${principal}")
