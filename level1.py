import math
"""
"""
def answer(n):
	primes = ''
	for num in range(1, 101):
		if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
			primes += str(num)
	print primes
	return primes[n+1:n+6]
print answer(3)

