from scipy import stats

group_a = [2.1, 2.5, 1.8, 2.4, 2.0, 2.3, 1.9]
group_b = [2.5, 2.7, 2.8, 2.6, 2.9, 2.4, 2.7]

t_statistic, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)
print(f"T-test statistic: {t_statistic}")
print(f"P-value: {p_value}")
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in means.")
else:
    print("Fail to reject the null hypothesis: No significant difference in means.")
    
