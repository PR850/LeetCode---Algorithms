
def isPalindrome(x):
    try:
        if x == int(str(x)[::-1]):
            return True
        else:
            return False
    except:
        return False
