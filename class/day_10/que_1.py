import pandas as pd

data = pd.read_csv("class/day_10/rainfall.csv")
df = pd.DataFrame(data)
print(df)

# 1. How many missing values are present in each column of the dataset?
print(df.isnull().sum())

# 2. What percentage of data is missing in each year or region?
print(df.isnull().mean() * 100)

# 3. Impact of dropping missing values on the dataset
df_dropped = df.dropna()
print("Impact of dropping missing values:", df_dropped)

# 4. Mean, median, and standard deviation of annual rainfall across all years
df_mean = df.describe()
print("Mean, Median, and Standard Deviation of Annual Rainfall:\n", df_mean)

# 5. Highest and lowest average annual rainfall by region/state
highest_rainfall = df.groupby("Subdivision")["Annual"].mean().idxmax()
lowest_rainfall = df.groupby("Subdivision")["Annual"].mean().idxmin()
print("Region with highest average annual rainfall:", highest_rainfall)
print("Region with lowest average annual rainfall:", lowest_rainfall)

# 6. Yearly trend in average rainfall
yearly_trend = df.groupby("Year")["Annual"].mean()
print("Yearly trend in average rainfall:\n", yearly_trend)

# 7. Total amount of rainfall recorded in India over the dataset period (1901-2015)
total_rainfall = df["Annual"].sum()
print("Total rainfall recorded in India (1901-2015):", total_rainfall)

# 8. Seasonal variation in rainfall
seasonal_rainfall = {
    "Winter (Jan-Feb)": df["Jan-Feb"].mean(),
    "Pre-Monsoon (Mar-May)": df["Mar-May"].mean(),
    "Monsoon (Jun-Sep)": df["Jun-Sep"].mean(),
    "Post-Monsoon (Oct-Dec)": df["Oct-Dec"].mean()
}
print(seasonal_rainfall)

# 9. Month with highest and lowest average rainfall
print(df[["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]].mean())


# 10. Regions with extreme seasonal variations
extreme_variations = df.groupby("Subdivision")["Annual"].std()
print("Regions with extreme seasonal variations:\n", extreme_variations)


# 11. Effect of filling missing values with different methods
df_filled_mean = df.copy()
numeric_cols = df.select_dtypes(include=['number']).columns
df_filled_mean[numeric_cols] = df_filled_mean[numeric_cols].fillna(df[numeric_cols].mean())
print("Effect of filling missing values with mean:\n", df_filled_mean)


# 12. Effect of filling missing values with median  
df_filled_median = df.copy()    
numeric_cols = df.select_dtypes(include=['number']).columns
df_filled_median[numeric_cols] = df_filled_median[numeric_cols].fillna(df[numeric_cols])
print(df_filled_median)

data = df_filled_mean
df.to_csv("class/day_10/rainfall.csv")
