from scipy import stats

alpha = 0.05

sample_data = [12,15,14,10,13,14,15,16,14,13]
population_mean = 13

t_stat_one,p_value_one = stats.ttest_1samp(sample_data, population_mean)

print(f"t-statistic: {t_stat_one:.4f}")
print(f"p-value: {p_value_one:.4f}")

if p_value_one < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
    
group1= [23,21,19,24,25]
group2= [27,29,26,30,28]

t_stat_two,p_value_two = stats.ttest_ind(group1, group2)

print(f"t-statistic: {t_stat_two:.4f}")
print(f"p-value: {p_value_two:.4f}")

if p_value_two < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
    
# The t-statistic is calculated as (sample_mean - population_mean) / (sample_std_dev / sqrt(sample_size))
# The p-value is the probability of observing a test statistic as extreme as the one calculated, under the null hypothesis.
# In this case, we are testing if the sample mean is significantly different from the population mean.
# The null hypothesis (H0) is that the sample mean is equal to the population mean.
# The alternative hypothesis (H1) is that the sample mean is not equal to the population mean.
# The t-test is used when the population standard deviation is unknown and the sample size is small (n < 30).
