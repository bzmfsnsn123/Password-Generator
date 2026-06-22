import random
import string
lover=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits

symbols=("!@#$%^&*()_+=")
all_char=symbols+lover+upper+num

use_upper=input("是否使用大写字母？y/n:").strip().lower()=='y'
use_num=input("是否使用数字？y/n:").strip().lower()=='y'
use_symbol=input("是否使用特殊字符？y/n:").strip().lower()=='y'
char_pool=lover
if use_upper:
    char_pool+=upper
if use_num:
    char_pool+=num
if use_symbol:
    char_pool+=symbols

try:
    length=int(input("请输入密码长度："))
    if length<4:
        print("错误:密码不能少于四位！")
    elif len(char_pool)==0:
        print("密码至少选择小写字母之外的一种字符！")
    else:
        final_pwd=""
        for _ in range(length):
            char=random.choice(char_pool)
            final_pwd+=char
        print(f"最终生成密码是:{final_pwd}")

except ValueError:
    print("输入错误需要输入数字哦")