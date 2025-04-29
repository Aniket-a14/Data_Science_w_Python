import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

x= np.array([[500],[750],[1000],[1250],[1500],[1750],[2000],[2250],[2500]])
y= np.array([150,200,250,275,300,325,350,375,400])

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.2, random_state=0)

model= LinearRegression()
model.fit(x_train, y_train)
y_pred= model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Coefficients:", model.coef_)

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_test, y_pred, color='red', label='Regression Line', linewidth=2)
plt.title('House Price Prediction: House Size vs Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($)')
plt.legend()
plt.grid(True)
plt.show()

a=np.array([[3500]])
predicted_price= model.predict(a)
print("Predicted price for house size 3500 sq ft:", predicted_price[0])

x_df = pd.DataFrame(x, columns=['House Size'])
vif_data = pd.DataFrame()
vif_data["feature"] = x_df.columns
vif_data["VIF"] = [variance_inflation_factor(x_df.values, i) for i in range(x_df.shape[1])]
print(vif_data)