A=[("dog","type"),("black","color"),("cat","type"),("blue","color"),("green","color"),("pig","type")]
B = dict(A)

for key,val in B.items():
    if val == 'color':
        print(key)