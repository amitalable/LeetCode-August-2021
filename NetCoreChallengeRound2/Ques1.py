from itertools import permutations


def solve(A, N, K):
    l = []
    for i in range(N):
        for j in range(N):
            l.append(abs(A[i]-A[j]))
    return l
    # hashMap = {}
    # for i in range(N):
    #     for j in range(N):
    #         x = abs(A[i]-A[j])
    #         if x in hashMap.keys():
    #             hashMap[x] += 1
    #         else:
    #             hashMap[x] = 1
    # x = 0
    # y = K
    # hashMap2 = {}
    # for i in sorted(hashMap):
    #     hashMap2[i] = hashMap[i]

    # for k, v in hashMap2.items():
    #     if x+v < y:
    #         x += v
    #         y -= x
    #     else:
    #         return k


print(solve([1, 2, 3], 3, 7))
