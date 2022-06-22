import matplotlib.pyplot as plt

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

# user inputted vars
principal = input('What is your base principal amount? ')
principal = float(principal)
formatted_dollars = "${:,.2f}".format(principal)
print(f'Okay, your starting principal is {formatted_dollars}.')

interest = input(f'What is your assumed avg % interest rate? ')
decimal_interest = float(interest) / 100
print(f'Nice, {interest}% interest.')

contribution = input('What is your total annual contribution? ')
contribution = float(contribution)
formatted_contribution = "${:,.2f}".format(contribution)
print(f'Excellent, contributing {formatted_contribution} a year will help your investments grow.')

growthYears = input('How many years before you retire? ')
print(f'{growthYears} years of growth, you\'ll be there before you know it!')

# display bar graph of investments over time
plt.title(f'Compound interest over {growthYears} years at {percentage}')
plt.bar(left, testInterest, tick_label = tick_label, width = .75, color = ['green']) # plotting a bar chart
plt.ylabel('Total value (by $Millions)') # naming the y-axis
plt.xlabel('Years of compounding')# naming the x-axis
plt.show() # function to show the plot chart