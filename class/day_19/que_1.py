import numpy as np
from scipy.stats import chi2_contingency

#Observed frequency table from your image
# Rows: [CS, Non-CS]
#Columns: [Python,Java,C++]

# observed = np.array([
#     [30,10,10],  #CS
#     [10,20,20]   #Non-CS
# ])

observed = np.array([
    [35, 52.5, 12.5], 
    [28.1, 42.1, 9.8],   
    [6.0, 10.4, 2.7]
])

#Perform the chi_square test
chi2_stat, p_value, dof, expected = chi2_contingency(observed)

#Display the results
print("Chi Square Test of Independencies")
print("-------------------------")
print(f"Chi-square Statistic: {chi2_stat:.4f}")
print(f"Degrees of Freedom:   {dof}")
print(f"P-value:              {p_value:.4f}")
print("\nExpected Frequencies:")
print(expected)

#Interpretation at 0.05 significance level
alpha = 0.05

if p_value < alpha:
    print("\nReject the null hypothesis: There is a significant association between CS and programming language preference.")
else:
    print("\nFail to reject the null hypothesis: There is no significant association between CS and programming language preference.")
    
# The chi-square test is used to determine if there is a significant association between two categorical variables.
# In this case, we are testing if there is a significant association between the CS major and the preferred programming language.
# The null hypothesis (H0) is that there is no association between the two variables, while the alternative hypothesis (H1) is that there is an association.
# The chi-square statistic measures how much the observed frequencies deviate from the expected frequencies under the null hypothesis.


#What is null hypothesis?
#The null hypothesis (H0) is a statement that there is no effect or no difference, and it serves as the default assumption in hypothesis testing.
# In the context of the chi-square test, the null hypothesis states that there is no association between the two categorical variables being tested.