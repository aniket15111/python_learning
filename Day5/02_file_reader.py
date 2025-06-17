try:
    with open("Day5/sample.txt","r")as file:
        a=file.read()
        print(a)
except FileNotFoundError:
    print("file not found")