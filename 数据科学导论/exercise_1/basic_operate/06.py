i = input("plz enter a number: ")
str = list(i)
temp = []
sum = 0
for j in str:
    sum = sum + int(j)
if (sum%2!=0):
    temp = reversed(list(str))
    for j in temp:
        print(j,end="")
else:
    print(i,end="")