num = int(input("enter a num:"))
order = len(str(num))
sum = 0
for i in str(num):
    sum = sum + int(i)**order
if num == sum:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")