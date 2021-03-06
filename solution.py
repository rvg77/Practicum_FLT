alpha = str(input())
u = str(input())

stack = list()


def new_dp(value):  # generating empty dp array
    ans = [[value for j in range(len(u) + 1)] for i in range(len(u) + 1)]
    return ans


def check(number):  # check error
    if len(stack) < number:
        print("ERROR")
        exit()


def dp_sum(dp1, dp2):  # union
    dp = new_dp(0)

    for left in range(len(u) + 1):
        for right in range(len(u) + 1):
            if dp1[left][right] or dp2[left][right]:
                dp[left][right] = 1

    return dp


def dp_multiply(dp1, dp2):  # concatenation
    dp = new_dp(0)

    for left in range(len(u) + 1):
        for right in range(left, len(u) + 1):
            for middle in range(left, right + 1):
                if dp1[left][middle] and dp2[middle][right]:
                    dp[left][right] = 1
                    break

    return dp


def dp_star(dp1):
    dp = new_dp(0)

    for left in range(len(u) + 1):
        for right in range(left, len(u) + 1):
            if left == right:
                dp[left][right] = 1

            for border in range(left, right + 1):
                if not dp[left][border]:
                    continue
                if dp1[border][right] == 1:
                    dp[left][right] = 1
                    break

    return dp


for character in alpha:
    if 'a' <= character <= 'c':
        dp = new_dp(0)

        for l in range(len(u)):
            if u[l] == character:
                dp[l][l + 1] = 1

        stack.append(dp)

    elif character == '0':
        dp = new_dp(0)
        stack.append(dp)

    elif character == '1':
        dp = new_dp(0)
        for i in range(len(u) + 1):
            dp[i][i] = 1

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
