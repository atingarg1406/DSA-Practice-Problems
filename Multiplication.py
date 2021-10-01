n=int(input())
m=int(input())
def multiplication(n,m):
    if n==0 or m==0:
        return 0
    elif(n<m):
        return multiplication(m,n)
    else:
        return n+multiplication(n,m-1)
print(multiplication(n,m))
