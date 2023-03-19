import random
num_tests = 10
test_data = []
count = 0
for i in range(num_tests) :
    b = random.randint(10, 1000)
    while count != i :
        for j in range(i) :
            if b != test_data[j]:
                count=count+1
                print("b= "+ str(b)+" and test_data[j]= "+ str(test_data[j])+ " count= " + str(count))   
            if b == test_data[j] :
                b = random.randint(1, 1000)
                count=0
                j=0
                print("b= "+ str(b)+" and test_data[j]= "+ str(test_data[j])+ " count= " + str(count))        
    test_data.append(b)
    count = 0
    with open("data_" + str(i+1) +".txt", "w") as f:
        f.write(str(test_data[i]))
