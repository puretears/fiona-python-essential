
# 输入一个整数
# 打印：这是一个有 ? 位的数字

# 请输入一个整数：12345
# 这是一个有 5 位的数字，它的每一位分别是 1, 2, 3, 4, 5。

'''          商      余数
12345 / 10   1234    5
1234  / 10   123     4
123   / 10   12      3
12    / 10   1       2
1     / 10   0       1
当商为 0 的时候，我们就不再继续除了

怎么能够得到一个数字的每一位：当商为 0 的时候，把余数逆序
'''
n = input("请输入一个整数：")
n = int(n)

quotient = n // 10
counter = 1

# 列表：存储一堆东西的变量
reminders = [n % 10]

while quotient != 0:
    reminders.append(quotient % 10)  # append 把参数添加到列表的末尾
    quotient = quotient // 10
    counter = counter + 1

print(f"这是一个有 {counter} 位的数字。")

# reminders
#  0  1  2  3  len(reminders) - 1  - 元素在列表中的位置
# [1, 2, 3, 4, 5]- 元素在列表中的值
# reminders[0] - 读取列表位置 0 的值
# reminders[1] - 读取列表位置 1 的值
# reminders[len(reminders) - 1] - 读取列表最后一个位置的值
#
# reminders[0] = 1
# reminders[3] = 4
# reminders[1] = 2
# reminders[2] = 3
# reminders[4] = 5
#
# len 函数 - 读取列表中元素的个数
# len(reminders) = 5
#
# reminders 列表中最后一个元素的位置 len(reminders) - 1
# ** 对于一个列表来说，它的最后一个元素的位置，len(列表名) - 1。**
# ** 对于一个列表来说，它的起始元素的位置永远都是 0. **
pos = 0
s = "它的每一位数字分别是 "
reminders.reverse()

while pos <= len(reminders) - 1:
    if pos != len(reminders) - 1:
        s = s + f"{reminders[pos]}, "
    else:
        s = s + f"{reminders[pos]}。"

    pos = pos + 1

print(s)


