import numpy

def step(v):
	if v >= 0:
		return 1
	else:
		return 0

def perceptron(x, w, b):
	v = numpy.dot(w, x) + b
	y = step(v)
	return y

def AND_perceptron(x):
    w = numpy.array([1, 1])
    b = -1.5
    return perceptron(x, w, b)

pelda1 = numpy.array([1, 1])
pelda2 = numpy.array([1, 0])
pelda3 = numpy.array([0, 1])
pelda4 = numpy.array([0, 0])

print("AND({}, {}) = {}".format(1, 1, AND_perceptron(pelda1)))
print("AND({}, {}) = {}".format(1, 0, AND_perceptron(pelda2)))
print("AND({}, {}) = {}".format(0, 1, AND_perceptron(pelda3)))
print("AND({}, {}) = {}".format(0, 0, AND_perceptron(pelda4)))