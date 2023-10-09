def factorial(num):
	solution = 1
	if num == 0:
		return solution
	
	while num >= 1:
		solution = solution * num
		num = num - 1
	# your code here
	return solution

print(factorial(48))