
f1 = open("file1.txt",'r')
f2 = open("file2.txt",'w')
count = f1.readlines()
for i in range(0,len(count)):
    if(i % 2 != 0):
        f2.write(count[i])
f2 = open("file2.txt",'r')
count1 = f2.read()
print("Odd lines:\n",count1)
f1.close()
f2.close()