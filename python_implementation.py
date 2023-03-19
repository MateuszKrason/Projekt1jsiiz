import time
import os
test_num=10

def my_hex(num):
    if num < 0:
        raise ValueError("hex() argument cannot be negative")
    hex_digits = "0123456789abcdef"
    result = ""
    while num > 0:
        digit = num % 16
        result = hex_digits[digit] + result
        num //= 16
    if result == "":
        result = "0"
    return "0x" + result

def main() :    
    for i in range(test_num):
        with open("data_" + str(i+1) +".txt", "r") as f:
            x = f.readline()
            x= int(x)
            print("liczba ", x)
            start_time = time.time_ns()
            hex(x)
            time.sleep(1)
            end_time = time.time_ns()
            print("hex() funct lasted: " + str((end_time-start_time-1000000)/(10**9)) + " miliseconds")
            start_time = time.time_ns()
            my_hex(x)
            time.sleep(1)            
            end_time = time.time_ns()
            with open("python_"+ str(i+1) + ".txt", "w") as f:
                f.write(str(my_hex(x))+"\n")
            print("my_hex() funct lasted: " + str((end_time-start_time-1000000)/(10**9)) + " miliseconds")
main()