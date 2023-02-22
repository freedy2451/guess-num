import random

r = random.randint(1,100)
while True:
    a = int(input("請輸入1~100來猜數字: "))
    if a == r:
        print("恭喜你猜到了")
        break
    elif a > r:
        print("數字比答案大")
    elif a < r:
        print("數字比答案小")      