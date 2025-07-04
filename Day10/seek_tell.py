with open("Day10/input.txt", "r") as f:
    print("Start position:", f.tell())
    line1 = f.readline()
    print("After reading one line:", f.tell())
    f.seek(0)
    print("After seek(0):", f.readline())

