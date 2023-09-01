"""

     search insert 
#*!        [ 1, 3, 5, 6 ], 3 == 1
#**        [ 1, 3, 5, 6 ], 4 == 2
#*?        [ 1, 3, 5, 6 ], 7 == 4
#TODO      [ 1, 3, 5, 6 ], 0 == 0

"""

def search_insert(array, value):
        low = 0
        high = len(array) - 1 #3
        mid = high // 2   #1
        
        while low <= high:
                if value > array[mid]:
                        mid += 1
                        low = mid 
                else:
                        mid -= 1
                        high = mid
                        
        return low

print(search_insert([1, 3, 5, 6], 0))
                        
        