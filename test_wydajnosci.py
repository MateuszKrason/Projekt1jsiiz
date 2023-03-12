from os import system
import random
import math
import time
import subprocess

num_tests = 1000
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
    subprocess.call(["cpp_implementation", str(data[0]), str(data[1])])
end_time = time.time()

print("C++ implementation: " + str(end_time - start_time) +" seconds")
