import numpy as np
from sklearn.linear_model import LinearRegression
n=1000
features = np.loadtxt('input.txt',max_rows=n)
test = np.loadtxt('input.txt',skiprows=n)
y = features[:,5].copy()
ones = np.ones(n)
features[:,5] = ones
X = np.array([features[:,i]*features[:,j] for i in range(6) for j in range(6)]).transpose()
reg = LinearRegression()
reg.fit(X, y)
b = np.zeros((n,6))
b[:, :-1] = test
b[:,5] = ones
X_test = np.array([b[:,i]*b[:,j] for i in range(6) for j in range(6)]).transpose()
np.savetxt('output.txt', reg.predict(X_test))