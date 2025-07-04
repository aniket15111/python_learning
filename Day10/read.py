a = open("Day10/input.txt", "r")
while True:
    line = a.readline()
    if not line:
        break
    print(line, end="")  

a.close()