from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# 去读数据文件  以 'rt'
allElectronicsData = open(r'E:/Java/python/DecisionTree/AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)
headers = next(reader)
print("表格头: " + str(headers))
featureList = []
labelList = []

for row in reader:  # row=[1,youth,high,no,fair,no]
    labelList.append(row[len(row) - 1])  # "no"
    rowDict = {}
    for i in range(1, len(row) - 1):  # range(1, 4) =1,2,3,4  =遍历 [ youth,high,no,fair ] rowID-剔除
        rowDict[headers[i]] = row[i]  # rowDict[RID]=1 rowDict[age]=youth ...map结构
    featureList.append(rowDict)

print("转化后目标:  " + str(featureList))  # [{'age': 'youth', 'income': 'high', 'student': 'no', 'credit_rating': 'fair'},...]
print("目标值:  " + str(labelList))
# Vetorize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()  # 转化成01变量,,age income...
print("转化后的特征变量名 " + str(vec.get_feature_names()))
print("转化后的特征变量值: " + str(dummyX))

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)  # 转化特征值
print("目标值转化成0 1变量:  " + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion='entropy')  # 实例化决策树
clf = clf.fit(dummyX, dummyY)  # 计算决策树参数值
print("clf: " + str(clf))

# Visualize model 可视化模型
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0, :]  # dummyX是二维的,oneRowX变一维
print("oneRowX: " + str(oneRowX))
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict([newRowX])  # 需要二维数据??
print("predictedY(预测结果,1:购买,2:不购买): " + str(predictedY))
