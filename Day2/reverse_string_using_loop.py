string="Hi my name is Aniket Kaushal"
# char_list=list(string)
# for i in range(0,int(len(string)/2)):
#     temp=char_list[i]
#     char_list[i]=char_list[len(char_list)-i-1]
#     char_list[len(char_list)-i-1]=temp
# print(''.join(char_list))    
reverse_string=""
for i in string:
    reverse_string=i+reverse_string
print(reverse_string)