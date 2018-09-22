# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
from chapter8 import ex71
import re


def remove_noise(words):
    from nltk.stem.porter import PorterStemmer as PS

    result = []
    ps = PS()
    for w in words:
        # ストップワードを除去
        if not ex71.is_stop_word(w) and len(w) > 1:
            # 各単語をステミング処理して登録する
            result += [ps.stem(w)]
    return result

if __name__ == "__main__":
    input_file_name = "sentiment.txt"
    output_file_name = "features.txt"
    enc = "utf-8"

    # 素性（=特徴量）を抽出する
    # 重複は無視するために集合として定義
    features = set()

    ptn = re.compile(r"[,.\n\d-]+")
    with open(input_file_name, "r", encoding=enc) as f:
        for line in f:
            words = ptn.sub("", line[3:]).split(" ")
            features.update(remove_noise(words))

            # ネガポジを分離する場合
            # tag = line[:2]
            # if tag == "+1":
            #     pos_features.update(remove_noise(words))
            # elif tag == "-1":
            #     neg_features.update(remove_noise(words))

    with open(output_file_name, "w", encoding=enc) as f:
        for feature in features:
            print(feature, file=f)
