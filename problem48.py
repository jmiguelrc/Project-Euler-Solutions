MAX = 1000;
NUM_DIGITS = 10;

result = 0

for i in range(1, MAX + 1):
	# Only need to keep the last 10 digits of each term
	result += (i**i) % (10**NUM_DIGITS)

# Only need to keep the last 10 digits of the result
result = result % (10**NUM_DIGITS)
print result
