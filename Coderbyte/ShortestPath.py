'''
Using the Python language, have the function ShortestPath(strArr) 
take strArr which will be an array of strings which models a 
non-looping Graph... 
https://www.python.org/doc/essays/graphs/
https://www.coderbyte.com/editor/guest:Shortest%20Path:Python

'''
from find_path import find_path

def ShortestPath(strArr):
    nodesNumber = int(strArr[0])
    strArr = strArr[1:]
    thisDict = {}
    for i in range(nodesNumber):
        thisDict[strArr[i]]=[]

    strArr = strArr[nodesNumber:]
    for j in range(len(strArr)):
        strTemp = strArr[j]
        startNode = strTemp[0]
        endNode = strTemp[2]
        for item in thisDict.items():
            if item[0]==startNode:
                item[1].append(endNode)

    print(thisDict)

    #print(find_path(thisDict,'A','D'))
    #print(find_path(thisDict,'A','F'))
    print(find_path(thisDict,'X','W'))

#myInput = ["6","A","B","C","D","E","F","A-B","A-C","B-C","B-D","C-D","D-C","E-F","F-C"]
#myInput = ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
myInput = ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]

ShortestPath(myInput)
                


