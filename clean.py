import os

num =10

for i in range(num+1) :
        os.system("rm -rf python_"+ str(i)+ ".txt")
        os.system("rm -rf data_"+ str(i)+ ".txt")
        os.system("rm -rf cpp_"+ str(i)+ ".txt")