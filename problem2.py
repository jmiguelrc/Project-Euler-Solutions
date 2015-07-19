def is_even(num):
	return (num % 2 == 0)

max = 4000000

new_fibonacci = 2
old_fibonacci = 1

total_sum = 0

while new_fibonacci < max:
	total_sum += is_even(new_fibonacci) * new_fibonacci

	to_be_old_fibonacci = new_fibonacci
	new_fibonacci = new_fibonacci + old_fibonacci
	old_fibonacci = to_be_old_fibonacci

print total_sum