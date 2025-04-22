from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

conv_rate = [50,65]
samples = [200,220]

z_test, p_value = proportions_ztest(conv_rate, samples)
print(f"Z-test statistic: {z_test}")
print(f"P-value: {p_value}")
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: No significant difference in conversion rates.")

