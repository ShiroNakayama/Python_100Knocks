# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
from chapter4 import ex30

connected_nouns = []
for sentence in ex30.read_mecab():
    for i, n in enumerate(sentence):
        if n["surface"] == "の":
            if sentence[i-1]["pos"] == "名詞" and sentence[i+1]["pos"] == "名詞":
                connected_nouns += [sentence[i - 1]["surface"] + n["surface"] + sentence[i + 1]["surface"]]

print(connected_nouns)
