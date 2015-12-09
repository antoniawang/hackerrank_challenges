# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_palindrome(strng):
    i = 0
    while i < len(strng)/2:
        if strng[i] != strng[-i-1]:
            return i
        else:
            i += 1
    return -1
        
def make_palindrome(strng):
    result = is_palindrome(strng)
    if result != -1:
        new_strng = strng[0:result] + strng[result+1:]
        if is_palindrome(new_strng) == -1:
            return result
        else:
            return len(strng) - result - 1
    else:
        return result
        
T = int(raw_input())
for _ in range(0, T):
    print make_palindrome(raw_input()) 