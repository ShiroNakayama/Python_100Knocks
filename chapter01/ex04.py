# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine.
#  New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
import re

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
         " New Nations Might Also Sign Peace Security Clause. Arthur King Can."
string = re.sub(r"[^a-zA-Z0-9 ]", "", string)

wordList = string.split(" ")
topGetter = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

count = 1
for w in wordList:
    if count in topGetter:
        result[w[0]] = count
    else:
        result[w[0:2]] = count
    count += 1

print(result)

# 冗長
for k, v in sorted(result.items(), key=lambda x: x[1]):
    print(k, end=" ")
