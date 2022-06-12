fish = 1
while True:
    total = fish
    flag = True
    for i in range(5):
        if (total-1) % 5 == 0:
            total = (total - 1) /5 * 4
        else:
            flag = False
            break
    if flag:
        print(fish)
        break
    fish = fish + 1
