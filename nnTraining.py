from nn import *
from TrainingData import *

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


size = 10000

#generate test data
data = orData(size)
# print(data.inputs)
# print(data.outputs)

#create neural network
nn = NeuralNetwork([3,5,5,1])

#train
for datum in range(0,size):
	# print(data.inputs[datum])	#inputs
	# print(data.outputs[datum])
	# print(nn.result(data.inputs[datum]))	# what it would give me
	nn.feedForward(data.inputs[datum])
	nn.backPropogation([data.outputs[datum]])	
	# nn.show(-1)	#the error



#test
print(nn.result([0,0,0]))
print(nn.result([0,0,1]))
print(nn.result([0,1,0]))
print(nn.result([0,1,1]))
print(nn.result([1,0,0]))
print(nn.result([1,0,1]))
print(nn.result([1,1,0]))
print(nn.result([1,1,1]))


# fig = plt.figure()
# ax = plt.axes(projection = '3d')
# x0 = np.linspace(0,1.1, 20)
# x1=x0

# X0, X1 = np.meshgrid(x0,x1)
# Z = np.zeros((len(x0),len(x1)))

# for a in range(0,len(x0)):
# 	for b in range(0,len(x1)):
# 		Z[a,b] = nn.result([a,b])

# ax.plot_surface(X0,X1,Z)
# plt.show()