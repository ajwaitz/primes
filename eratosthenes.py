"""
Simple Python implementation of the Sieve of Eratosthenes.
"""

def sieve(n):
	l = [False for i in range(n + 2)]
	l[0] = True
	l[1] = True
	p = 2

	while (True):	
		i = 2
		while p * i < n + 2:
			l[p * i] = True
			i += 1
		
		p_ = p

		for i in range(p + 1, n+2):
			if not l[i]:
				p = i
				break

		if p_ == p:
			return l

def print_primes(n = 100):
	out = sieve(n)
	for i in range(len(out)):
		if not out[i]:
			print(i)

if __name__ == '__main__':
	print_primes(100000)