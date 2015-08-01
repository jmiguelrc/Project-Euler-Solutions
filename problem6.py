N_NUMBERS = 100

sum_squares_result = 0
sum_result = 0

for i in range(1, N_NUMBERS + 1):
	sum_squares_result += i**2
	sum_result += i

print sum_squares_result
print sum_result**2
print sum_result**2 - sum_squares_result