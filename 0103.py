import random # 生成随机数的工具

'''
1. 要让计算机随机生成一个数字

2. 我们要猜这个数字
2.1 如果我们猜的这个数字比计算机生成的数字大，提示用户说你猜大了
2.2 反之我们就提示用户：你猜小了

只要用户没有猜对的话，我们就要提示完用户之后，让他一直猜

2.3 猜的等于计算机随机生成的，我们就提示用户：恭喜你，猜对了。

当用户猜对了，我们就让程序结束
'''
def guess_number():
    num = random.randint(1, 1000)

    while True:
        guess = input("请你猜一个数字: ") # guess 是一个字符串
        guess = int(guess) # "199" => 199

        if guess > num:
            print("你猜大了。")
        elif guess < num:
            print("你猜小了。")
        else: # guess == num
            print("你猜对了。")
            break

    print("游戏结束")

'''
如何在程序里完成因数分解

12 (1, 12)
2 - 从最小的因数开始尝试 - 是 ✅
6
2 - ✅
3
2 - ❌
3 - ✅
--- 尝试的因数和要找的数字本身相等了

7
2 - ❌
3 - ❌
4 - ❌
5 - ❌
6 - ❌
7 - ✅

'''
num = input("请输入一个要因数分解的数字：")
num = int(num)

divider = 2

while divider <= num:
    # 通过循环在这里不断的查找因数

    if num % divider == 0:
        # 找到了一个因数
        print(f"因数: {divider}")
        num = num / divider
        divider = 2
    else:
        divider = divider + 1

