def staircase(n):
    if n<3:
        return n
    if n==3:
        return 4 
    return staircase(n-1) + staircase(n-2) + staircase(n-3)
n=int(input())
count=staircase(n)

print(count)
