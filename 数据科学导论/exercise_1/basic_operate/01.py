a = input("plz enter number (1<=A<=9):")
b = input("plz enter number (1<=B<=10):")
while(int(a)<1 or int(a)>10 or int(b)<0 or int(b)>11 ):
    a = input("plz enter number (1<=A<=9):")
    b = input("plz enter number (1<=B<=10):")
for i in range(0,int(b)):
    print(a,end="")