# 87. 単語の類似度
# 85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
# ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
from chapter9 import ex86


def calc_cosine_similarity(vector1, vector2):
    """
    コサイン類似度を計算する
    :param vector1:
    :param vector2:
    :return:
    """
    from numpy.linalg import norm
    size1 = norm(vector1)
    size2 = norm(vector2)
    if size1 != 0 and size2 != 0:
        result = vector1 @ vector2 / (size1 * size2)
    else:
        result = -1
    return result


if __name__ == "__main__":
    trg_word1 = "United_States"
    trg_word2 = "U.S"

    # 単語文脈行列を読み込む
    X_300 = ex86.load_matrix()
    index_t = ex86.load_index_t()

    # 対象2単語のコサイン類似度を計算する
    cosine_similarity = calc_cosine_similarity(X_300[index_t[trg_word1]], X_300[index_t[trg_word2]])
    print(cosine_similarity)
