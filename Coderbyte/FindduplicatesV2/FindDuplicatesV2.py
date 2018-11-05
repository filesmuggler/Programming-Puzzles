'''
https://www.coderbyte.com/algorithm/find-duplicates-in-array-linear-time-v2
(1) Loop through the array
(2) At each element check if it exists in the hash table, which has a lookup of O(1) time
(3) If the element exists in the hash table then it is a duplicate, if it doesn't exist, 
    insert it into the hash table, also O(1)

'''
# returns the arrary of duplicates
def FindDuplicatesV2(arr):
    # dictionary to store information
    # if the object has been already
    # encountered
    hashTable = {}

    # table to store duplicated elements
    dupsTable = []

    # if an element is already, dump it to dups
    for item in arr:
        if item not in hashTable:
            hashTable[item] = True
        else:
            dupsTable.append(item)

    return dupsTable


print(FindDuplicatesV2([2,3,3,2,-2,1,5,6,9]))
    