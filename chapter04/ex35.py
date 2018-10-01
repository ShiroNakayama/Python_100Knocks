# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
from chapter04 import ex30

connected_nouns = []
is_multiple = False
temp = ""
for sentence in ex30.read_mecab():
    for n in sentence:
        if n["pos"] == "名詞":
            if temp != "":
                is_multiple = True
            temp += n["surface"]
        else:
            if is_multiple:
                connected_nouns += [temp]
            is_multiple = False
            temp = ""

print(connected_nouns)
