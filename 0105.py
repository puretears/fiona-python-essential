
# 丑数 Ugly number

# 输入一个正整数，如果这个正整数，它的质因数只有2，3 或 5，那么这个数字就叫做丑数。

# 6 = 2 * 3 - 丑数
# 14 = 2 * 7 - 不是丑数
# 12 = 2 * 2 * 3 - 丑数

# 1 - 规定 1 是丑数

# 写一个程序，输入一个数字，
# - ?? 是丑数
# - ?? 不是丑数

# 1. 输入一个正整数
number = input("请输入一个正整数：")
number = int(number)
num = number

# 2. 对 number 进行质因数分解
divider = 2
is_ugly_number = True # 布尔变量

while divider <= number:
    # 判断 divider 是不是 number 的质因数
    if number % divider == 0:
        print(f"因数是 {divider}")
        if divider != 2 and divider != 3 and divider != 5:
            is_ugly_number = False
            print(f"{num} 不是丑数。")
            break

        number = number // divider
    else:
        divider = divider + 1

# ..
if is_ugly_number:
    print(f"{num} 是丑数。")