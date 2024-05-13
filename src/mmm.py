from scipy import stats
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Mean
m = numpy.mean(speed)
#Median
md = numpy.median(speed)
#mode
mo = stats.mode(speed)
print(m)
print(md)
print(mo)

