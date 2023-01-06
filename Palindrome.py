
# Palindrome
# 回文
# 如果一个字符串，它从左向右读，和从右向左读，结果一样，那么这个字符串就叫做回文。
#
# "10101" ✅
# "bob", "abba", "xyyx" ✅
# "abc" - ❌

# 变量名要尽可能表达创建它的意图

# 输入一个字符串
input_string = input("请输入一个字符串：")

'''
字符串是一种特殊的列表
a - input_string[0] 
b - input_string[1]
b - input_string[2] 
a - input_string[3]
              vR=len(input_string) - 1
a b a a a a b a
^L=0
        
L >= R 的时候表示 input_string 是一个回文
'''

# 输出这个字符串是不是回文
l = 0
r = len(input_string) - 1
is_palindrome = True

while l < r:
    if input_string[l] == input_string[r]:
        l = l + 1
        r = r - 1
    else:
        is_palindrome = False
        # 说明 input_string 不是回文
        print(f"{input_string} 不是回文。")
        break

if is_palindrome:
    print(f"{input_string} 是回文。")
