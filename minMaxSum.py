'''
Question:"Min-Max Sum"
Given five positive integers, find the minimum and maximum values that can be calculated by summing 
exactly four of the five integers. Then print the respective minimum and maximum values as a single 
line of two space-separated long integers.
'''
#Solution
def miniMaxSum(arr):
    totalSum=0
    minVal=arr[0]
    maxVal=arr[0]
    for i in arr:
        totalSum+=i
        if i<minVal:
            minVal=i
        if i>maxVal:
            maxVal=i
    minSum = totalSum - maxVal
    maxSum = totalSum - minVal
    print(minSum, maxSum)

    
