import subprocess

test_number = 1

while True:
    try:
        file = open("./system_tests/test" + str(test_number) + ".txt", 'r')

    except Exception:
        print("OK", test_number - 1, "tests passed")
        exit()

    result = subprocess.run(["python3", "Solution.py"], stdin=file, stdout=subprocess.PIPE)

    with open("./system_tests/answer" + str(test_number) + ".txt", 'r') as ans:
        if result.stdout.decode("ascii") != ans.read():
            print("WA" + str(test_number))
            exit()

    file.close()
    test_number = test_number + 1
