import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([1000,1500,2000,2500,3000]).reshape(-1,1)
y = np.array([200,300,400,500,600])

model = LinearRegression().fit(X,y)

print(f"y={model.coef_[0]:.2f}x + {model.intercept_:.2f}")
print(f"Predicted:${model.predict([[2200]])[0]:.2f} thousand")
