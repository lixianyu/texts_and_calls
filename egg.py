import math
# f = open('my_file.txt','w')
# f.write("Hello world!")
# f.close()
'''
with open('my_file.txt','r') as f:
    file_data = f.read(5)
    fd2 = f.read(3)
    print("file_data = {}".format(file_data))
    print("fd2 = {}".format(fd2))
'''
print(math.factorial(4))

import multiprocessing as mp
print("There are %d CPU" % mp.cpu_count())
