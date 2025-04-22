from scipy.stats import uniform, binom, poisson
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mean=100
a=0
b=30
x1=0
x2=10
prob= uniform.cdf(x2, loc=a, scale=b-a)- uniform.cdf(x1, loc=a, scale=b-a)
print("Uniform Distribution Probability:", prob)

sd=5
size=100000
data= np.random.normal(mean, sd, size)
sns.histplot(data, kde=True)
plt.show()

n=10
p=0.5
k=6
prob= binom.pmf(k, n, p)
print("Binomial Distribution Probability:", prob)


a=3
k=5
prob= poisson.pmf(k, a)
print("Poisson Distribution Probability:", prob)