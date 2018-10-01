# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．
from chapter04 import ex30


def extract_nouns():
    """
    Mecabの形態素解析結果から名詞を抽出する
    :return: 名詞の形態素リスト
    """
    morphemes = ex30.read_mecab()
    nouns = []
    for sentence in morphemes:
        for m in sentence:
            if m["pos"] == "名詞":
                nouns += [m]

    return nouns

if __name__ == "__main__":
    # サ変接続の名詞を抽出
    verbal_nouns = []
    for n in extract_nouns():
        if n["pos1"] == "サ変接続":
            verbal_nouns += [n]

    print([vn["surface"] for vn in verbal_nouns])
