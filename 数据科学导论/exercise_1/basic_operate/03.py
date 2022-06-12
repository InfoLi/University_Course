sentence = input()
str = list(sentence)
temp = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    temp[i] = str[i]
new_list=[]
for i in str:
    if i not in new_list:
        new_list.append(i)
if len(str)==len(new_list):
    for i in str:
        print(i,end=" ")
else:
    print("not found")

    
