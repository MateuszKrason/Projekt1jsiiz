from os import system
import random
import math
from s180450_proj1_v1 import popr
import subprocess


num_tests = 10
test_data = []

for i in range(num_tests):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    test_data.append((a, b))

for i, data in enumerate(test_data):
    with open("test_" + str(i+1) +".txt", "w") as f:
        f.write(str(data[0]) + " " + str(data[1]))

    with open("python_"+ str(i+1) + ".txt", "w") as f:
        result = math.gcd(data[0], data[1])
        f.write(str(result))

    # system("g++ -o cpp cpp_implementation.cpp")
    x = subprocess.call(["cpp_implementation", str(data[0]), str(data[1])])
    print(str(x))
    with open("cpp_" + str(i+1) + ".txt", "w") as f:
        f.write(str(x))

for i in range(num_tests) :
    with open("cpp_" + str(i+1) + ".txt", "r") as cpp:
        with open("python_"+ str(i+1) + ".txt", "r") as pyth:
            test1 = cpp.readlines()
            test2 = pyth.readlines()
            if test1 == test2 :
                with open("output.txt", "w") as outp:
                    outp.write("all correct")
            else :
                with open("output.txt", "w") as outp:
                    outp.write("something went wrong")
