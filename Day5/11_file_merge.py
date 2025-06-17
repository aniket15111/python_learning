with open("Day5/sample.txt",'r') as file:
    a=file.read()
print(a)

with open("Day5/sample2.txt",'a')as file:
    file.write(a)


