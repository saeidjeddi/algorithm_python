"""

Polynomial  Time  O( n ^ 2 )

"""

nums = [44,65,11,90,300,20,10,9]

def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j] , collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection

print(bubble_sort(nums))