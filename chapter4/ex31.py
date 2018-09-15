# 31. 動詞
# 動詞の表層形をすべて抽出せよ．
from chapter4 import ex30


def extract_verbs():
    """
    Mecabの形態素解析結果から動詞を抽出する
    :return: 動詞の形態素リスト
    """
    morphemes = ex30.read_mecab()
    verbs = []
    for sentence in morphemes:
        for m in sentence:
            if m["pos"] == "動詞":
                verbs += [m]

    return verbs

if __name__ == "__main__":
    verbs_surface = []
    for verb in extract_verbs():
        verbs_surface += [verb["surface"]]

    print(verbs_surface)
