# Enter your code here. Read input from STDIN. Print output to STDOUT
def funny_str(str):
    rev_str = str[::-1]
    for i in range(1,len(str)):
        if abs(ord(str[i])-ord(str[i-1])) != abs(ord(rev_str[i]) - ord(rev_str[i-1])):
        	return "Not Funny"
    return "Funny"


T = int(raw_input())
for _ in range(0,T):
    print funny_str(raw_input())
	print funny_str(x)