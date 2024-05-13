import numpy
import matplotlib.pyplot as plt

# Histogram
# Generation of synthetic data for testing
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5, color = "hotpink")
plt.show()