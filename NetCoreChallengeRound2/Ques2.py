n = 6
val = [3, 3, 4, 5, 6, 2]
par = [1, 1, 2, 2, 5]


def mex(arr):
    arr.sort()
    if arr[0] != 1:
        return 1
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != 1:
            return arr[i-1]+1
    return arr[len(arr)-1]+1


def solve(n, val, par):

    # val = [3,2,2,4,2]
    # par = [1,1,2,2,5]
    hashMap = {1: [val.pop(0)]}
    l = [mex(hashMap[1])]
    for i in range(n-1):
        hashMap[i+2] = hashMap[par[i]] + [val[i]]
        l.append(mex(hashMap[i+2]))
    return l


print(solve(n, val, par))
