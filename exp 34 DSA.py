from sklearn.linear_model import LinearRegression

X = [[100,10],[120,8],[150,6],[180,5]]
y = [8,9,11,13]

m = LinearRegression().fit(X,y)

print("Price:", round(m.predict([[140,7]])[0],2))
