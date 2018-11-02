from find_weighted_path import find_weighted_path

def WeightedPath(strArr):
    # dictionary to hold points and paths
    graphDict = {}

    # number of different keys
    numNodes = int(strArr[0])
    strArr = strArr[1:]
    
    # getting keys to the dictionary
    for i in range(numNodes):
        graphDict[strArr[i]]=[]
    
    strArr = strArr[numNodes:]
    for j in range(len(strArr)):
        strTemp = strArr[j]
        startNode = strTemp[0]
        endNode = strTemp[2]
        nodeWeight = strTemp[4]
        for item in graphDict.items():
            if item[0]==startNode:
                dataTuple = (endNode,nodeWeight)
                item[1].append(dataTuple)

    print(graphDict)


myInput = ["4","X","Y","Z","W","X|Y|2","Y|Z|3","X|W|1"]

WeightedPath(myInput)