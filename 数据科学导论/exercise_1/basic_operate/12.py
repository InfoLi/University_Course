num = input("enter a number: ")
sum = 1
for i in range(1,int(num)+1):
    sum = sum*i
print("%d! = %d"%(int(num),sum))