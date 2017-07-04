def steps(n):
    if n <= 0:
        return 1
    else:
        return steps(n-1)+steps(n-2)+steps(n-3)

def stepsDyna(n):
    if n <= 0:
        return 1
    memo = []
    for x in range(0, n):
        minimemo = [-1, -1, -1]
        memo.append(minimemo)
    if memo[n-1][0] == -1:
        memo[n-1][0] = stepsDyna(n-1)
    if memo[n-1][1] == -1:
        memo[n-1][1] = stepsDyna(n-2)
    if memo[n-1][2] == -1:
        memo[n-1][2] = stepsDyna(n-3)
    return memo[n-1][0] + memo[n-1][1] + memo[n-1][2]

print stepsDyna(25)
print steps(25)
