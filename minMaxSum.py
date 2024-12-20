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

    