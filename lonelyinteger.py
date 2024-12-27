'''
Question:
Given an array of integers, where all elements but one occur twice, find the unique element.
Note: This problem also can solved in better option. which is "Bit Manipulation"
'''
def lonelyinteger(a):
    unique=[]
    for i in a:
        if i in unique:
            unique.remove(i)
        else:
            unique.append(i)
    return unique.pop()
