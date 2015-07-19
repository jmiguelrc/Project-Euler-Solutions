def minimum_number_divisible(divisors_until = 20):
	number = divisors_until
	while True:
		for div in range(1, divisors_until + 1):
			if (number % div != 0):
				break
			if (div == divisors_until):
				return number
		number += 2
	return 0

minimum = minimum_number_divisible(20)
print minimum