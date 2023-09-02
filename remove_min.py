"""
    remove min
    
    [3, 5, 8, 10, 11, 1] ==> remove  1


"""


def remove_min(stack):
    storages_stack = []
    if len(stack) == 0:
        return stack

    min = stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val

        storages_stack.append(val)

    for i in range(len(storages_stack)):
        val = storages_stack.pop()
        if val != min:
            stack.append(val)

    return stack, min


print(remove_min([3, 5, 8, 10, 11, 1]))