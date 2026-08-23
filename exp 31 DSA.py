from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X = [[1,2],[2,3],[8,9],[9,8]]
y = [0,0,1,1]

m = KNeighborsClassifier(3).fit(X,y)
p = m.predict(X)

print("Accuracy:", accuracy_score(y,p))
