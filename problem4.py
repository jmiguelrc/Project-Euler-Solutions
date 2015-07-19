def is_palindrome(num):
	num_str = str(num)

	for i in range(len(num_str) // 2):
		if num_str[i] != num_str[-i-1]:
			return False
	return True

x_max = 1000
y_max = 1000

max_palindrome = 999

for x in range(x_max):
	for y in range(y_max):
		if is_palindrome(x*y) and x*y > max_palindrome:
			max_palindrome = x*y

print max_palindrome