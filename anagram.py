# Enter your code here. Read input from STDIN. Print output to STDOUT
def make_anagram(strng):
    if len(strng)%2 == 1:
        return -1
    else:
        count = 0
        S1 = strng[0:len(strng)/2]
        S2 = strng[len(strng)/2:]
        dict1 = {}
        dict2 = {}
        for a in S1:
            dict1.setdefault(a,0)
            dict1[a] += 1
        for b in S2:
            dict2.setdefault(b,0)
            dict2[b] += 1
        count = 0
        for key in dict2:
            diff = dict2[key] - dict1.get(key,0)
            if diff > 0 :
                count += diff
                
        return count
                
            

T = int(raw_input())
for _ in range(0,T):
    print make_anagram(raw_input())