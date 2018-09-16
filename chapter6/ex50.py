# 英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
# 50. 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
# 入力された文書を1行1文の形式で出力せよ．
import re


def separate_sentence():
    """
    (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
    nlp.txtを1行ごとに分割する。
    :return: 各要素が1文に対応するリスト
    """
    file_name = "nlp.txt"
    regex = re.compile(r"(.*?[.;:?!])\s([A-Z].*)")
    new_doc = []
    with open(file_name) as f:
        for line in f:
            while True:
                match = regex.match(line)
                if match is not None:
                    # 残りが2文以上の場合
                    new_doc += [match.group(1)]
                    line = match.group(2)
                else:
                    # 残りが1文だけの場合
                    if line != "\n":  # 改行だけの行は無視
                        new_doc += [line]
                    break
    return new_doc

if __name__ == "__main__":
    # print(new_doc)
    for l in separate_sentence():
        print(l)
