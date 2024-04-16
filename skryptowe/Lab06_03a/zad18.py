# 18. Zdefiniuj funkcję reverse_str() do odwracania stringu.

def reverse_str(str:str):
    res = ""
    for i in range(len(str)-1, -1, -1):
        res += str[i]
    return res

print(reverse_str("ala ma kota"))
