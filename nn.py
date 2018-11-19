import numpy as np

class NeuralNetwork:
	def __init__(self, layers):
		self.layers = layers
		self.weights = [None]*(len(layers)-1)
		self.biases = []
		inputs = layers[0] #number of inputs will number of neurons in input layers
		#initilize weights and biases
		for hiddenLayer in range(1,len(layers)):	#start at the first hidden layer
			self.weights[hiddenLayer-1] = np.random.random_integers(-100,100, (layers[hiddenLayer] , layers[hiddenLayer - 1])  )/100	#make weights between -1 and 1
			self.biases.append( np.random.random_integers(-100,100, (layers[hiddenLayer] , 1) )/100 )	#make biases between -1 and 1

	def feedForward(self, inputs):
		self.z = [None]*len(self.layers)
		self.z[0] = np.array(inputs).reshape(-1,1)		# covert to column vector
		for hiddenLayer in range(1,len(self.z)):	#start at the first hidden layer
			#output of next layer = weights from inputs from L-1 * inputs from L-1 + biases from L
			self.z[hiddenLayer] =  np.matmul( self.weights[hiddenLayer-1] , self.z[hiddenLayer -1] ) + self.biases[hiddenLayer - 1]
		
		self.a = [None]*len(self.z)
		for zLayer in range(0,len(self.z)):	
			self.a[zLayer] = self.sigmoid( self.z[zLayer] )# calculate activation

	def sigmoid(self, x):
		return 1/(1+np.exp(-x))

	def dsigmoid(self, x):
		return self.sigmoid(x)*(1-self.sigmoid(x))

	def backPropogation(self, expectedOutput):
		self.expectedOutput = np.array(expectedOutput).reshape(-1,1)

		#error
		self.delta = [None]*len(self.layers)
		#deltaL = (aL - y) . dsig(zL)
		self.delta[-1] = np.multiply(  np.subtract( self.a[-1], self.expectedOutput), self.dsigmoid(self.z[-1])  )	#error at last position
		for layer in range(len(self.z)-2,-1,-1): 	#looping through all layers backwards starting from L-1 since L has a special formula
			self.delta[layer] = np.multiply( np.matmul( np.transpose(self.weights[layer]), self.delta[layer+1]  ),  self.dsigmoid(self.z[layer]) )

		# #change in bias
		self.deltaBiases = self.delta[1:] 	#change in biases  = error

		# #change in weights
		self.deltaWeights = [None]*len(self.weights)
		for layer in range(0,len(self.weights)):
			self.deltaWeights[layer] = np.matmul(self.delta[layer+1], np.transpose( self.a[layer] ))
		
		#self.deltaWeights[layer] = np.transpose( np.matmul( self.a[layer], np.transpose(self.delta[layer+1])  ) )

		self.weights = np.subtract(self.weights, self.deltaWeights)
		self.biases = np.subtract(self.biases, self.deltaBiases)

	def result(self, inputs):
		self.feedForward(inputs)
		return self.sigmoid(self.z[-1])

	def show(self, index):	#for debugging
		print(self.delta[index])
