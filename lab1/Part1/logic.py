#!/usr/bin/env python3

# ---------------  1 --------------------------
# first_name = input("please enter first name")
# last_name = input("please enter last name")
# print(f"welcome {last_name} {first_name}")

# --------------- 2 --------------------------

# n = input("please enter your favorite number")
# n1 = int("%s" %n)
# n2 = int("%s%s" %(n,n))
# n3 = int("%s%s%s" %(n,n,n))
# print(n1+n2+n3)

# -------------- 3 ---------------------------

# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example """)

# -------------- 4 ---------------------------

# pi = 3.14 
# r = 6
# v = 4/3*pi*r**3
# print(f"The volume of the sphere with radius {r} is : {v}")

# -------------- 5 ---------------------------

# base = float(input("please enter the base  "))
# height = float(input("please enter the height  "))
# triangle_area = (base*height)/2
# print(f"The area of the triangle with base {base} and {height} is {triangle_area}")


# -------------- 6 ---------------------------

# n=5
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print(' ')
    
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")




# -------------- 7 ---------------------------
# word = input("please enter a word to reverse it  ")
# reversed_word = word[::-1]
# print(f"the reversed word is {reversed_word}")


# -------------- 8 ---------------------------

# for n in range(6):
#     if(n==3 or n==6):
#         continue
#     print(n,end=' ')

# -------------- 9 ---------------------------
# x,y=0,1

# while (y<50):
#     print(y,end=' ')
#     x=y
#     y=x+y


# -------------- 10 ---------------------------
# digits = 0
# letters = 0

# string = input("please enter any string:  ")

# for character in string:
#     if character.isdigit():
#         digits = digits +1
#     elif character.isalpha():
#         letters = letters +1
#     else:
#         continue

# print(f"digits is {digits}")
# print(f"letters is {letters}")