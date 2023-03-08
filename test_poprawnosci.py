from os import system
import random
import math

num_tests = 10
test_data = []

for i in range(num_tests):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    test_data.append((a, b))

for i, data in enumerate(test_data):
    with open(f"test_{i+1}.txt", "w") as f:
        f.write(f"{data[0]} {data[1]}")

    with open(f"python_{i+1}.txt", "w") as f:
        result = math.gcd(data[0], data[1])
        f.write(str(result))

    system("g++ -o cpp gcd.cpp")
    with open(f"cpp_{i+1}.txt", "w") as f:
        system(f"./cpp {data[0]} {data[1]} > output.txt")
        with open("output.txt", "r") as f2:
            result = f2.read().strip()
            f.write(result)
