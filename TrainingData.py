import random as rd

class xorData:
	def __init__(self, size):
		self.inputs = [None]*size
		self.outputs = [None]*size
		for i in range(0,size):
			self.inputs[i] = [ rd.randint(0,1), rd.randint(0,1) ]
			a = self.inputs[i][0]
			b = self.inputs[i][1]
			self.outputs[i] = int((not a and b) or (a and not b))

class andData:
	def __init__(self, size):
		self.inputs = [None]*size
		self.outputs = [None]*size
		for i in range(0,size):
			self.inputs[i] = [ rd.randint(0,1), rd.randint(0,1) ]
			a = self.inputs[i][0]
			b = self.inputs[i][1]
			self.outputs[i] = int(a and b)

class orData:
	def __init__(self, size):
		self.inputs = [None]*size
		self.outputs = [None]*size
		for i in range(0,size):
			self.inputs[i] = [ rd.randint(0,1), rd.randint(0,1) ]
			a = self.inputs[i][0]
			b = self.inputs[i][1]
			self.outputs[i] = int(a)

class orData:
	def __init__(self, size):
		self.inputs = [None]*size
		self.outputs = [None]*size
		for i in range(0,size):
			self.inputs[i] = [ rd.randint(0,1), rd.randint(0,1), rd.randint(0,1) ]
			a = self.inputs[i][0]
			b = self.inputs[i][1]
			c = self.inputs[i][1]
			self.outputs[i] = int( (a and b) or c )