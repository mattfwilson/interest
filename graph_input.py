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
# while yearCounter < growthYears:
#     yearCounter += 1
#     principal, interestDelta = calcInterest(principal, interest, numCompounds, contribution)
#     principal = round(principal, 2)
#     interestDelta = round(interestDelta, 2)
#     testInterest.append(principal)

principal = input('What is your base principal amount? ')
print(f'Okay, your starting principal is ${principal}.')
interest = input(f'What is your assumed avg % interest rate? ')
decimal_interest = float(interest) / 100
print(f'Nice, {interest}%.')
contribution = input('What is your total annual contribution? ')
print(f'Excellent, ${contribution} will help your investment grow.')
growthYears = input('How many years before you retire? ')
print(f'{growthYears}, you\'ll be there before you know it!')

# show chart
plt.title(f'Compound interest over {growthYears} years at {percentage}')
plt.bar(left, testInterest, tick_label = tick_label, width = .75, color = ['green']) # plotting a bar chart
plt.ylabel('Total value (by $Millions)') # naming the y-axis
plt.xlabel('Years of compounding')# naming the x-axis
plt.show() # function to show the plot chart