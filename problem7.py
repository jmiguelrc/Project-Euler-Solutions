PRINT_ORDERED_DIGIT = 10001

LIST_PRIMES = list()
LIST_PRIMES.append(1)
cur = 2

while (len(LIST_PRIMES) < PRINT_ORDERED_DIGIT):
    is_prime = True
    for prime in LIST_PRIMES[1:]:
        if (cur % prime == 0):
            is_prime = False
            break
    if (is_prime):
        LIST_PRIMES.append(cur)
        if (len(LIST_PRIMES) % 100 == 0):
            print "Prime #" + str(len(LIST_PRIMES)) + ":   " + str(cur)
    cur = cur+1

print "Prime #" + str(PRINT_ORDERED_DIGIT) + ":   " + str(LIST_PRIMES[PRINT_ORDERED_DIGIT - 1])