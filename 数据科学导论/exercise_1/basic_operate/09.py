num = input("")
num_list = num.split(" ")
new_list = []
for i in num_list:
    if(int(i)%2==0):
        new_list.append(i)

for i in new_list:
    print(i,end=" ")