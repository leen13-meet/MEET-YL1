def palindrome():
	x= raw_input("Write a word")
	if x== x[::-1]:
		return True
	else:
		return False
print palindrome()








"""def palindrome():
	x= raw_input()
	xLen= len(x)
	for counter in xrange (xLen/2):
		if x[counter]== x[xLen-counter-1]:
			return True
		else:
			return False
palindrome()"""
