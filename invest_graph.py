import matplotlib.pyplot as plt
from matplotlib import pylab

# variables to play with
principal = 600000
interest = .065
numCompounds = 12
yearCounter = 0
growthYears = 10
contribution = 36000
testYears = []
testInterest = []

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
    testYears.append(interestDelta)
    print(f'Year {yearCounter} Total: ${principal} | Interest: ${interestDelta}')
    print(f'{testInterest}')

left = [1, 2, 3, 4, 5] # x-coordinates of left sides of bars
height = [10, 24, 36, 40, 5] # heights of bars
tick_label = ['one', 'two', 'three', 'four', 'five'] # labels for bars

# plot title
percentage = "{:.2%}".format(interest)
plt.title(f'Compound interest over {growthYears} years at {percentage}')
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['orange', 'green']) # plotting a bar chart
plt.ylabel('Value in dollars') # naming the y-axis
plt.xlabel('Years of compounding')# naming the x-axis
plt.show() # function to show the plot chart