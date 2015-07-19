def is_prime(num):
	for x in range(2, num):
		if (num % x == 0):
			return False
	return True

def find_primes_until(num = 1000):
	primes = list()

	for x in range(2, num):
		if is_prime(x):
			primes.append(x)
	return primes

rest = 600851475143
primes_factors = list()

primes = find_primes_until(10000)

while rest != 1:
	for prime in primes:
		if (rest % prime == 0):
			primes_factors.append(prime)
			rest = rest / prime
			break

print max(primes_factors)