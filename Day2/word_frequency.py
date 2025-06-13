sentence="hi hello hi good morning hello"
unique={}
sentence_list=sentence.lower().split()
for i in sentence_list:
    if i in unique:
        unique[i]+=1
    else:
        unique[i]=1

for i,j in unique.items():
        print(f"{i} appears {j} times")
