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
    with open("test_" + str(i+1) +".txt", "w") as f:
        f.write("{data[0]} {data[1]}")

    with open("python_"+ str(i+1) + ".txt", "w") as f:
        result = math.gcd(data[0], data[1])
        f.write(str(result))

    system("g++ -o cpp cpp_implementation.cpp")
    with open("cpp_" +str(i+1) + ".txt", "w") as f:
        system("cpp {data[0]} {data[1]} > output.txt")
        with open("output.txt", "r") as f2:
            result = f2.read().strip()
            f.write(result)
