"""
        is isomorphic 
                foo, bar == False
                foo, boo == True
                fow , boo 
                
                {f:b, o:e, w:e}  (b, e, e)
                
"""


def is_isomorphic(s, t):
    if len(s)!= len(t):
        return False
    
    dict = {}
    se_values = set()
    
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in se_values:
                return False
            dict[s[i]] = t[i]
            se_values.add(t[i])
        else:
            if dict[s[i]]!= t[i]:
                return False
            
        
    return  True  #dict, se_values

print(is_isomorphic("fow", "bor"))