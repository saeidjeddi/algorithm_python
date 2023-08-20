"""

[ 1, 2, 3, 4, 5 ]

# *!            min 3 ==> [3, 4, 5]
# *?            max 3 ==> [1, 2, 3, 4]
                min, max ==> [3]

"""

def limit(arr, min=None, max=None):
    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)
    
    return [val for val in arr if min_check(val) and max_check(val)]

print(limit([1, 2, 3, 4, 5], 2))


#=============================================================================

# def limit(arr, min=None, max=None): 
#     l = []
    
#     if min:
#         for val in arr:
#             if val >= min:
#                 l.append(val)
                
#     if max:
#         for val in arr:
#             if val <= max:
#                 l.append(val)
                
#     print(l)
    
    
# limit([1, 2, 3, 4, 5,], min=2)