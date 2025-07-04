a=open("Day10\log.txt",'a')
b=""
while (b!="esc"):
    a.write(f"{b} \n")
    b=input("Enter the value you want to write")

a.close()
