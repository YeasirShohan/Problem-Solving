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