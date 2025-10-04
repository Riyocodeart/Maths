import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1000,2],[1500,3],[2000,3],[25000,4],[3000,4]])
y = np.array([200,300,350,500,550])

model = LinearRegression().fit(X,y)
coefs = model.coef_
intercept = model.intercept_

print(f"y ={intercept:.2f} + {coefs[0]:.2f}*size + {coefs[1]:.2f}*bedrooms")
print(f"Predicted(2200 sq ft, 3 beds):${model.predict([[2200,3]])[0]:.2f} thousand")
