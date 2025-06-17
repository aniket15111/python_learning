from datetime import datetime as dt
dt1=dt.now().strftime("%Y-%m-%d %H:%M")
a=input("Enter what you want to add in a file")
a=f"\n[ {dt1}] {a}"
print(a)
with open("Day5/sample.txt",'a') as file:
    file.write(a)
    print("File saved")