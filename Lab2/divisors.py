def divisors():
	n = int(raw_input("enter a number"))
	for num in range(1,n+1):
		if n % num == 0:
			print num
divisors()
