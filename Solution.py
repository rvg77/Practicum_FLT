alpha = str(input())
u = str(input())

stack = list()


def empty_dp():  # generating empty dp array
    ans = [[0 for j in range(len(u) + 1)] for i in range(len(u) + 1)]
    return ans


def check(number):  # check error
    if len(stack) < number:
        print("ERROR")
        exit()


def dp_sum(dp1, dp2):  # union
    dp = empty_dp()

    for left in range(len(u)):
        for right in range(len(u) + 1):
            if dp1[left][right] or dp2[left][right]:
                dp[left][right] = 1

    return dp


def dp_multiply(dp1, dp2):  # concatenation
    dp = empty_dp()

    for left in range(len(u)):
        for right in range(len(u) + 1):
            if left > right:
                continue
            for middle in range(left, right + 1):
                if dp1[left][middle] and dp2[middle][right]:
                    dp[left][right] = 1
                    break

    return dp


def dp_star(dp1):
    dp = empty_dp()

    for left in range(len(u)):
        for right in range(len(u), -1, -1):
            if left == right:
                dp[left][right] = 1

            for period in range(left + 1, right + 1):
                if (right - left) % (period - left):
                    continue
                if not dp1[left][period]:
                    continue
                if u[left:right] == u[left:period] * int((right - left) / (period - left)):
                    dp[left][right] = 1
                    break

    return dp


for character in alpha:
    if 'a' <= character <= 'c':
        dp = empty_dp()

        for l in range(len(u)):
            if u[l] == character:
                dp[l][l + 1] = 1

        stack.append(dp)

    elif character == 0:
        dp = empty_dp()
        stack.append(dp)

    elif character == 1:
        dp = empty_dp()
        for i in range(len(u)):
            dp[i][i + 1] = 1
        stack.append(dp)

    elif character == '+':
        check(2)
        y = stack.pop()
        x = stack.pop()
        stack.append(dp_sum(x, y))

    elif character == '.':
        check(2)
        y = stack.pop()
        x = stack.pop()
        stack.append(dp_multiply(x, y))

    else:
        check(1)
        x = stack.pop()
        stack.append(dp_star(x))

if len(stack) != 1:
    print("ERROR")
    exit()

dp = stack.pop()

for left in range(len(u)):
    if dp[left][len(u)]:
        print(len(u) - left)
        exit()

print(0)
