# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_med(listofnum):
    nums = sorted(listofnum)
    idx = len(nums)/2
    return nums[idx]

N = int(raw_input())
X = [int(x) for x in raw_input().split()]
print find_med(X)