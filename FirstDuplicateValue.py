# Big O notation - O(n**2) Time | O(1) space

#find the duplicated value that occurs first in the given array

#brute-force
def FirstDuplicateValue(array):
    #In this case the length of the array is 7 and we are calling it 'minimumSecondIndex'
    minimumSecondIndex = len(array)
    # we are looping through the array once and calling each integer 'value'
    for i in range(len(array)):
        value = array[i]
        #this loop will go through the array 7 times, incrementing up one integer per loop and calling each iterated integer 'valueToCompare'
        for j in range(i + 1, len(array)):
            valueToCompare = array[j]
            #this added feature in the loop checks if the initial 'value' (i) is the same as the 'valueToCompare' (j) is equal.
            #if so, it assigns the minimumSecondIndex as  
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)
            

    if minimumSecondIndex == len(array):
        return "nope"

    return array[minimumSecondIndex]

result = FirstDuplicateValue([2,1,5,2,3,3,4])
print(result)


# O(n) Time | O(n) space
# second solution
# def FirstDuplicateValue(array):
#     seen = set()
#     for value in array:
#         if value in seen:
#             return value
#         seen.add(value)
#     return -1

# result = FirstDuplicateValue([2,1,5,2,3,3,4])
# print(result)

# O(n) Time | O(1) space
# final solution
# def FirstDuplicateValue(array):
#     for value in array:
#         absValue = abs(value)
#         if array[absValue - 1] < 0:
#             return absValue
#         array[absValue - 1] *= -1
#     return -1

# result = FirstDuplicateValue([2,1,5,2,3,3,4])
# print(result)