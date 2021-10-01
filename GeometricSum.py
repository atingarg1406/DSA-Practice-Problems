def geosum(n):
    if n<0:
        return 0
    return 1/pow(2,n) + geosum(n-1)
n=int(input())
geosum(n)
print("{:.5f}".format(geosum(n)))
