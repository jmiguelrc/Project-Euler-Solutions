def find_multiples_3_5(max = 1000):
	multiples = list()

	for x in range(max):
		if (x % 3 == 0 or x % 5 == 0):
			multiples.append(x)

	return multiples


result = 0
multiples = find_multiples_3_5(1000)

for multiple in multiples:
	result += multiple

print result