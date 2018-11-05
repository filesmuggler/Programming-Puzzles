/**
 * https://www.coderbyte.com/algorithm/find-duplicates-in-array-linear-time-v2
 * (1) Loop through the array 
 * (2) At each element check if it exists in the hash table, which has a lookup of O(1) time 
 * (3) If the element exists in the hash table then it is a duplicate, if it doesn't exist, 
 *     insert it into the hash table, also O(1)
 */

 function FindDuplicatesV2(arr){
     var hashTable = [];
     var dupsTable = [];

     for(var i = 0; i<arr.lenght; i++){
         if(hashTable[arr[i].toString()]===undefined){
             hashTable[arr[i].toString()] = true;
         }
         else{
             dupsTable.push[arr[i]];
         }
     }
     return dupsTable;
 }

 FindDuplicatesV2([1, -21, 2, 2, 3]);