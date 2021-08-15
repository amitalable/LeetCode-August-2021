arr = [[1, 2, 4], [2, 3, 1], [3, 4, 1], [4, 5, 3], [3, 5, 2]]
# arr = [[1, 2, 5], [2, 3, 4], [4, 3, 2]]
m = 5
n = 5


def findRichPoor(arr, n):
    ##borrower = []
    hashMap = {}
    path = {}
    rich_path = {}
    for x, y, w in arr:
        # borrower.append(y)
        hashMap[y] = hashMap.get(y, 0) + w
        rich_path[x] = rich_path.get(x, 0) + w
        if x in path:
            path[x].append(y)
        else:
            path[x] = [y]
    print(rich_path)
    max_v = 0
    rich = 0
    for k, v in rich_path.items():
        if v > max_v:
            max_v = v
            rich = k

    max_v = 0
    poor = 0
    for k, v in hashMap.items():
        if v > max_v:
            max_v = v
            poor = k
    return (rich, poor, path)


def generatePath(path, arr, v, vec):
    if not path:
        return
    vec.append(v)
    if v not in path:
        arr.append(vec[:])
        return

    for i in path[v]:
        generatePath(path, arr, i, vec)
    del path[v]


def MoneyPath(arr, m, n):
    rich, poor, path = findRichPoor(arr, n)
    print(path)
    path = {1: [2], 2: [3], 3: [4, 5, 6], 4: [5], 6: [7]}
    arr = []
    generatePath(path, arr, 1, [])
    print("arr", arr)
    l = []
    x = ""
    for k, v in path.items():
        x = x + str(k)
        for i in v:
            st = x + str(i)
            l.append(st)
            if st[0] == str(rich) and st[-1] == str(poor):
                list(map(int, st[::-1]))
    print(l)
    return [-1]


print(MoneyPath(arr, m, n))
