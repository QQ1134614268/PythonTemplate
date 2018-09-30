import csv
# Read in the csv file and put features into list of dict and list of class label
 
allElectronicsData = open(r'001.csv', 'rt')
 
reader = csv.reader(allElectronicsData)
print(reader)
headers =  next(reader)
 
print(headers)
 
featureList = []
labelList = []
 
for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
 
print(featureList)