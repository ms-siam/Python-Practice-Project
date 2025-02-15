#Generate a random integer from 0 to 100
'''from numpy import random

x = random.randint(100)

print(x)

#Generate Random Float
xf = random.rand()

print(xf)

#Generate a 1-D array containing 5 random integers from 0 to 100:
xia=random.randint(100, size=(5))

print(xia)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
xia2 = random.randint(100, size=(3, 5))

print(xia2)

#Generate a 1-D array containing 5 random floats:
xfa = random.rand(5)

print(xfa)

#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
xfa2 = random.rand(3, 5)
print(xfa2)

#Return one of the values in an array:
xrva = random.choice([3, 5, 7, 9])

print(xrva)

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
xrva2 = random.choice([3, 5, 7, 9], size=(3, 5))

print(xrva2)

xrdd = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(xrdd)

xrdd2 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(xrdd2)

from numpy import random
import numpy as np

#shuffling arrays
arrs = np.array([5, 6, 7, 8, 9])
random.shuffle(arrs)
print(arrs)

#Generating Permutation of Arrays

arrp = np.array([1, 2, 3, 4, 5])
print(random.permutation(arrp))
print(arrp)

#seaborn module
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

#Plotting a distplot without the histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

#Generate a random normal distribution of size 2x3:

from numpy import random

x = random.normal(size=(2, 3))
print(x)

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2

from numpy import random

xwls = random.normal(loc= 1, scale= 2, size= (2,3))
print(xwls)

#Visualization of normal distrbution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size = 1000), hist = False)

plt.show()

#Binomial Distribution
# Given 10 trials for coin toss generate 10 data points:
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)'''

#Visualization of binomial Distribution

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size=1000), kind= "kde")
plt.show()'''

#Difference between Normal and Binomial Distribution
'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#Use kdeplot instead of displot because displot doesn't support multiple plots in same figure
sns.kdeplot(random.normal(loc=50,scale=5, size=1000), label='normal')
sns.kdeplot(random.binomial(n=100, p=0.5, size=1000), label='binomial')
plt.legend()   #It shows the label in plot
plt.show()

#Poisson Distribution
#Generate a random 1x10 distribution for occurrence 2:
from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

#Visualization of Poison Distribution

from numpy import random

import matplotlib.pyplot as plt

import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))
plt.show()

#Difference between Normal and Poisson Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Use kdeplot instead of displot because displot doesn't support multiple plots in same figure
sns.kdeplot(random.normal(loc=50,scale=7, size=1000), label='normal')
sns.kdeplot(random.poisson(lam=50, size=1000), label='poisson')

plt.legend()  #It shows the label in plot
plt.show()

# Difference between Binomial and Poisson Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Use kdeplot instead of displot because displot doesn't support multiple plots in same figure
sns.kdeplot(random.binomial(n=1000,p=0.01, size=1000), label='normal')
sns.kdeplot(random.poisson(lam=10, size=1000), label='poisson')

plt.legend()  #It shows the label in plot
plt.show()

#Uniform Distribution
#Create a 2x3 uniform distribution sample:
from numpy import random
x=random.uniform(size=(2,3))
print(x)

# Visualization of Uniform Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(low=3, high=5, size = 1000), kind="kde")   #From 3 to 5 
sns.displot(random.uniform(size = 1000), kind="kde")   #From 0 to 1
plt.show()

#Logistic Distribution

#Draw 2x3 samples from a logistic distribution with mean at 1 and staddev 2.0:
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

#Visualization of logistic Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=1000), kind="kde")
plt.show()

#Difference between Normal and Logistic Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Use kdeplot instead of displot because displot doesn't support multiple plots in same figure
sns.kdeplot(random.normal(scale=2, size=1000), label='normal')
sns.kdeplot(random.logistic(size=1000), label='logistic')

plt.legend()   #It shows the label in plot
plt.show()

#Multinomial Distribution

#Draw out a sample for dice roll:

from numpy import random

x = random.multinomial(n=6, pvals=[1/6,  1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

#Exponential Distribution

#Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:

from numpy import random

x = random.exponential(scale = 2, size=(2, 3))

print(x)

#Visualization of Exponential Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.exponential(size=1000), kind="kde")
plt.show()'''

#Chi square distribution
'''
#Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:

from numpy import random
x=random.chisquare(df = 2, size=(2,3))
print(x)

#Visualization of Chi Square Distribution


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df =1, size = 1000), kind="kde")
plt.show()

#Rayleigh Distribution
#Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:

from numpy import random
x=random.rayleigh(scale = 2, size=(2,3))
print(x)

#Visualization of Rayleigh Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size = 1000), kind="kde")
plt.show()

#Pareto Distribution
#Draw out a sample for pareto distribution with shape of 2 with size 2x3:

from numpy import random
x=random.pareto(a = 2, size=(2,3))
print(x)

##Visualization of Pareto Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size = 1000), kde=False)
plt.show()'''

#Zipf Distribution

#Draw out a sample for czipf distribution with distribution parameter 2 with size 2x3:

from numpy import random
x=random.zipf(a = 2, size=(2,3))
print(x)

#Visualization of Zipf Distribution

#Sample 1000 points but plotting only ones with value<10 for more meaningful chart.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])
plt.show()