
def opening_file():
    with open('Day5/sample.txt','r') as file:
        f1=file.read()
        return f1
    
def word_count(b):
    c=b.split()
    a={}
    for i in c:
        if(i not in a):
            a[i]=1
        else:
            a[i]+=1
    d=sorted(a.items(),key=lambda x:x[1],reverse=True)
    print (d)
b=opening_file()
word_count(b)



