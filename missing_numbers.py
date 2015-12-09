# Enter your code here. Read input from STDIN. Print output to STDOUT
def ismissing(a,b):
    a_dict = {}
    b_dict = {}
    for x in a:
        a_dict.setdefault(x,0)
        a_dict[x] += 1
    for y in b:
        b_dict.setdefault(y,0)
        b_dict[y] += 1
    missing_list = []
    for key in b_dict:
        if key not in a_dict:
            missing_list.append(key)
        elif a_dict[key] < b_dict[key]:
            missing_list.append(key)       
    print ' '.join([str(num) for num in sorted(missing_list)])
    
N = int(raw_input())
A = [int(x) for x in raw_input().split()]
M = int(raw_input())
B = [int(x) for x in raw_input().split()]

ismissing(A,B)