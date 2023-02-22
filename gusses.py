import random

start = int(input("請輸入起始值"))
end = int(input("請輸入結束值"))
r = random.randint(start, end)

count = 0
while True:
    count += 1
    a = int(input("請輸入數字來猜答案: "))
    if a == r:
        print("恭喜你猜到了")
        print("這是你猜的第{}次".format(count))    
        break
    elif a > r:
        print("數字比答案大")
    elif a < r:
        print("數字比答案小")    
    print("這是你猜的第{}次".format(count))    