import math
from scipy.stats import norm

sample_mean = 169.5
population_mean = 168
population_std_dev = 3.9
sample_size = 36
alpha = 0.05
tail = 'two'

standard_error = population_std_dev / math.sqrt(sample_size)
z_score = (sample_mean - population_mean) / standard_error

if tail == 'two':
    p_value = 2 * (1 - norm.cdf(abs(z_score)))
    print(norm.cdf(abs(z_score)))
elif tail == 'left':
    p_value = norm.cdf(z_score)
elif tail == 'right':
    p_value = 1 - norm.cdf(z_score)
else:
    raise ValueError("Invalid tail type. Use 'two', 'left', or 'right'.")

print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")

# Decision rule
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")



#Z-test = (sample_mean - population_mean) / (population_std_dev / math.sqrt(sample_size)) 
#T-test = (sample_mean - population_mean) / (sample_std_dev / math.sqrt(sample_size))
# Assuming a normal distribution, we can use the Z-test for large sample sizes
