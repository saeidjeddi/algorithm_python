"""
Top One 
    [ 1, 2, 1, 3, 4, 2 ] ==> [1, 2]

"""


def top(arr):
    valus = {}
    result = []
    f_val = 0

    for i in arr:
        if i in valus:
            valus[i] += 1
        else:
            valus[i] = 1
    f_val = max(valus.values())

    for i in valus.keys():
        if valus[i] == f_val:
            result.append(i)
        else:
            continue

    return result, valus


print(top([1, 2, 3, 1, 3]))
