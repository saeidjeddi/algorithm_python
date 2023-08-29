from string import ascii_letters


def encrypt(string, key):
    alpha = ascii_letters
    result = ""

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result

print(encrypt("hello", 2))


def decrypt(string, key):
    key *= -1
    return encrypt(string, key) 
print(decrypt("jgnnq", 2))

def brute_force(string):
    alpha = ascii_letters
    key = 1
    result  = ""
    brute_force_data = {}
    
    while key <= len(alpha):
        result = decrypt(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1
    return brute_force_data

print(brute_force("jgnnq"))
