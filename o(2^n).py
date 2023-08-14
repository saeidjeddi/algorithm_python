"""

Exponential Time O(2^n)

"""

from itertools import chain, combinations

def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


print (list(subsets(['a','b'])))