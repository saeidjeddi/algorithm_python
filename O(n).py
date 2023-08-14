"""
Linear Time Series O(n)

"""

num = [1,4,5,55,7,8,47,1000,115,1125]

def show(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num
    
print(show(num))
    