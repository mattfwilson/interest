import matplotlib.pyplot as plt
from matplotlib import pylab

# variables to play with
principal = 0
interest = 0
percentage = "{:.2%}".format(interest)
numCompounds = 12
yearCounter = 0
growthYears = 10
contribution = 36000
testDollars = []
testInterest = []
interestDelta = []
left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # x-coordinates of left sides of bars
height = [10, 24, 36, 40, 5] # heights of bars
tick_label = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # labels for bars

# calculate compound interest
def calcInterest(principal, interest, numCompounds, contribution):
	accrued = (principal * (1 + (interest / numCompounds)) ** numCompounds) - principal
	principal = principal + accrued
	principal += contribution
	return principal, accrued

# show YOY summary
while yearCounter < growthYears:
    yearCounter += 1
    principal, interestDelta = calcInterest(principal, interest, numCompounds, contribution)
    principal = round(principal, 2)
    interestDelta = round(interestDelta, 2)
    testInterest.append(principal)
    # =print(f'Year {yearCounter} Total: ${principal} | Interest: ${interestDelta}')

# # find delta of YOY compound interest gains
# for i in range(1, len(testInterest)):
#     delta = testInterest[i] - testInterest[i - 1]
#     dollars = '${:,.2f}'.format(delta)
#     testDollars.append(dollars)
# print(f'Delta is {dollars}')
# print(testInterest)
# print(testDollars)

# show chart
plt.title(f'Compound interest over {growthYears} years at {percentage}')
plt.bar(left, testInterest, tick_label = tick_label, width = .75, color = ['green']) # plotting a bar chart
plt.ylabel('Total value (by $Millions)') # naming the y-axis
plt.xlabel('Years of compounding')# naming the x-axis
plt.show() # function to show the plot chart