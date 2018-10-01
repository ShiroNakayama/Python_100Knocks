# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
# ただし，文の終端では空行を出力せよ．
from chapter06 import ex50


def separate_words():
    """
    空白を単語の区切りとみなし，単語ごとに分割する。
    :return: 各要素が1単語に対応するリスト
    """
    doc = ex50.separate_sentence()
    words = []
    for line in doc:
        line = line.replace(",", "")
        line = line.replace(".", "")
        line_words = line.split(" ")
        if "\n" in line_words[-1]:
            line_words[-1] = line_words[-1].replace("\n", "")
            line_words += [" "]
        words += line_words

    return words

if __name__ == "__main__":
    for l in separate_words():
        print(repr(l))
