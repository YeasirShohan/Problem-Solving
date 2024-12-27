def lonelyinteger(a):
    unique=[]
    for i in a:
        if i in unique:
            unique.remove(i)
        else:
            unique.append(i)
    return unique.pop()