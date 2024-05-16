import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn import metrics
from preprocessing import loadData
import matplotlib.pyplot as plt
import matplotlib as mpl

xs = [i for i in range(1, 5)]
ys = []
for i in range(1, 5):
    avg = 0
    mses = []
    for j in range(0, 10):
        X, Y, testX, testY = loadData(tensor=False)
        testData = testX
        poly = PolynomialFeatures(degree=i)
        X_ = poly.fit_transform(X)
        testX_ = poly.fit_transform(testX)
        clf = linear_model.LinearRegression()
        clf.fit(X_, Y)
        mse = metrics.mean_squared_error(testY, clf.predict(testX_))
        avg += mse
        mses.append(mse)
    ys.append(avg/10)
    # print("ALL MSES FOR DEGREE: " + str(i) + " = " + str(mses))
    print("AVG MSE FOR DEGREE: " + str(i) + " = " + str(avg / 10))
fig, ax = plt.subplots()
ax.scatter(xs, ys)
ax.set_title("Mean Squared Error For Polynomial Regression")
ax.set_xlabel("Degree of Regression Equation")
ax.set_ylabel("Mean Squared Error")
plt.show()