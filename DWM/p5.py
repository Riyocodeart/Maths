import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[2,8],[3,6],[5,7],[1,5],[6,8]])
y = np.array([0,0,1,0,1])

model = GaussianNB().fit(X,y)

pred = model.predict([[4,7]])[0]
probs = model.predict_proba([[4,7]])[0]

print(f"Predicted: {'pass' if pred == 1 else 'fail'}")
print(f"P(Pass): {probs[1]:.2f}, P(Fail): {probs[0]:.2f})")