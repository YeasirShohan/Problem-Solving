'''
Question:"Plus Minus"
Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a new line with  places 
after the decimal.
'''

#Solution
def plusMinus(arr):
    pval=0
    nval=0
    zval=0
    total=len(arr)
    for i in arr:
        if(i>0):
            pval+=1
        elif(i==0):
            zval+=1
        else:
            nval+=1
    print(pval/total)
    print(nval/total)
    print(zval/total)
