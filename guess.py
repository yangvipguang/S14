# Author: yangvipguang
a = 22

guess = int(input("guess_age:"))

if guess == a:
    print("yes you got it")
elif guess > a :
    print("think smaller")
elif guess < a:
    print("think biiger")