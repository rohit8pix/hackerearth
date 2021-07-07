import math
def find (k, n):
    p  = math.ceil(math.sqrt(n))
    ans = p+(p-1)*(k-1)
    return ans

n, k = map(int, input().split())

out_ = find(k, n)
print(out_)
