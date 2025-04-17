from scipy.stats import ttest_ind


group_a = [23,43,58,69]
group_b = [12,42,96,103]

t,p = ttest_ind(group_a, group_b,equal_var=True)

print(f"t-statistic: {t:.4f}")
print(f"p-value: {p:.4f}")

if p < 0.05:
    print("Reject the null hypothesis: There is a significant difference between the two groups.")
else:  
    print("Fail to reject the null hypothesis: There is no significant difference between the two groups.")