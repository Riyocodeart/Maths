import numpy as np
from sklearn.tree import DecisionTreeClassifier

X = np.array([[2,8],[3,6],[5,7],[1,5],[6,8]])
y = np.array([0,0,1,0,1])

model = DecisionTreeClassifier(criterion='entropy').fit(X,y)

print(f"study importance:{model.feature_importances_[0]:.2f}")
print(f"Sleep importance:{model.feature_importances_[1]:.2f}")

pred = model.predict([[4,7]])[0]
print(f"Predicted:{'Pass' if pred ==1 else 'Fail'}")
