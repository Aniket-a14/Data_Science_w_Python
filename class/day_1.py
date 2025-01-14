import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "india_housing_prices.csv"
df = pd.read_csv(file_path)


print("Dataset Overview:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe(include='all'))

plt.figure(figsize=(10, 6))
sns.histplot(df['Price_in_Lakhs'], bins=50, kde=True, color='blue')
plt.title("Distribution of Property Prices (in Lakhs)", fontsize=16)
plt.xlabel("Price (in Lakhs)", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.show()