import pandas as pd

student = [1,2,3,4,5]
maths = [87,90,89,78,89]
science = [78,89,90,89,90]

dict1 = dict({"Student":student,"Maths":maths,"Science":science})

df = pd.DataFrame(dict1)

print(df.corr())
print(df.cov())