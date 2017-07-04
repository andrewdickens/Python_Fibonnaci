
def fibdyna(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo = []
    for x in range(0, n):
        memo.append(-1)
    if memo[n - 1] == -1:
        memo[n - 1] = fibdyna(n - 1)
    if memo[n - 2] == -1:
        memo[n - 2] = fibdyna(n - 2)
    return memo[n - 1] + memo[n - 2]

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

print(fibdyna(35))

print(fib(35))
