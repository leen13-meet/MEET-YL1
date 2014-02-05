class Integer(object):
	def __init__(self, num, positive):
		self.num= num
		self.p= positive

	def display(self):
		print self.p + str(self.num)

class NegativeInteger(Integer):
	def __init__(self, num):
		super(NegativeInteger, self).__init__(num, "-")

if __name__=="__main__":
	test1= NegativeInteger(9)
	test = Integer(9, "+")
	test1.display()
	
