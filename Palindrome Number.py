def palindrome(x):
    if x < 0:
        return False
    string = str(x)
    string = string[::-1]
    x1 = int(string)
    if x == x1:
        return True
    else:
        return False
