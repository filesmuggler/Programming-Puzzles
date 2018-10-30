'''
Using the Python language, have the function ArrayAddition(arr) 
take the array of numbers stored in arr and return the string 
true if any combination of numbers in the array (excluding the 
largest number) can be added up to equal the largest number in 
the array, otherwise return the string false... 

'''

def ArrayAddition(arr):
    max_num = arr[0]
    arr = arr[1:]
    sum_num = 0
    for number in arr:
        if(number>max_num):
            sum_num += max_num
            max_num = number
        else:
            sum_num += number

    if(sum_num == max_num):
        return True
    else:
        return False


#array = [3,7,7,2]
#print(ArrayAddition(array))
