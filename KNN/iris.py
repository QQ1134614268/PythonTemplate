from sklearn import neighbors
from sklearn import datasets
# 最邻近算法

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()
# save MNIST_data
# f = open("iris.MNIST_data.csv", 'wb')
# f.write(str(iris))
# f.close()
print (iris)

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]]) 
#print ("predictedLabel is :" + predictedLabel)
print (predictedLabel)