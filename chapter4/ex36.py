# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
from chapter4 import ex30
# from collections import Counter  # Counterクラスを使った方がシンプルに書ける


def count_words():
    counters = dict()
    for sentence in ex30.read_mecab():
        for n in sentence:
            if n["surface"] in counters:
                counters[n["surface"]] += 1
            else:
                counters[n["surface"]] = 1

    # 出現頻度の高い順に並べて返す
    return [item for item in sorted(counters.items(), key=lambda x: x[1], reverse=True)]

if __name__ == "__main__":
    print(count_words())


