counter = 15
percent = .07
total = 1579
interest = 0

while counter > 0:
	interest = total * percent
	total = total + interest 
	print(total)
	counter -= 1