def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    a = 0
    while i<len(s):
        if s[i].isupper():
            a+=1
        i+=1
    return a
print(main("Fifa World Cup Brazil"))