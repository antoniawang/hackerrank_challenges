# Enter your code here. Read input from STDIN. Print output to STDOUT
def gem_elements(n):
    gems_set = set(raw_input())
    for i in range(1,n):
        rock_set = set(raw_input())
        gems_set = gems_set.intersection(rock_set)
    return len(gems_set)

N = int(raw_input())
print gem_elements(N)