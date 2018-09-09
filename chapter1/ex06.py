# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
import chapter1.ex05 as func

str_x = "paraparaparadise"
str_y = "paragraph"

X = set(func.make_char_n_gram(str_x, 2))
Y = set(func.make_char_n_gram(str_y, 2))

print("X = " + str(X))
print("Y = " + str(Y))

print("X + Y = " + str(X | Y))
print("X * Y = " + str(X & Y))
print("X - Y = " + str(X - Y))
print("Y - X = " + str(Y - X))

obj_bi_gram = "se"
print(obj_bi_gram in X)
print(obj_bi_gram in Y)
