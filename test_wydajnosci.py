from os import system
import random
import math
import time

num_tests = 100000
test_data = []

for i in range(num_tests):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    test_data.append((a, b))

start_time = time.time()
for data in test_data:
    result = math.gcd(data[0], data[1])
end_time = time.time()

print("Python implementation: " + str(end_time - start_time) +" seconds")

start_time = time.time()
for data in test_data:
    # with open("output.txt", "w") as output_file:
    #     output_file.seek(0)
    #     output_file.write(str(data[0]) + " " + str(data[1]))
    system('g++ cpp_implementation.cpp -o cpp_implementation')
    system("cpp_implementation {data[0]} {data[1]} > output.txt")
end_time = time.time()

print("C++ implementation: " + str(end_time - start_time) +" seconds")
