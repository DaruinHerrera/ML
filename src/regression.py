# Linear Regression
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

"""
This relationship - the coefficient of correlation - is called r.
The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.
https://github.com/scipy/scipy
"""
slope, intercept, r, p, std_err = stats.linregress(x, y)
print('Relationship r, not perfect, but it indicates that we could use linear regression in future predictions.', r)

def myfunc(x):
  return slope * x + intercept

#Predict the speed of a 10 years old car
speed = myfunc(10)
print('Predicted a speed at ', speed)

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()