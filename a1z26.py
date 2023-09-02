"""
        a1z26
                saeed <===> [ 115, 97, 101, 101, 100 ]

chr , ord

"""


def encode(plain):
    return [ord(elm) - 92 for elm in plain]


def decode(encode):
    return "".join((chr(elm + 92) for elm in encode))


print(encode('saeed'))
print(decode([23, 5, 9, 9, 8]))
