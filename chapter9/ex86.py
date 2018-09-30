# 86. 単語ベクトルの表示
# 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
# ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
from scipy import io


def load_matrix():
    """
    単語文脈行列とそのインデックスを読み込む
    :return: 単位文脈行列(疎行列）
    """
    return io.loadmat("word_context_matrix_dim300")["X_300"]


def load_index_t():
    # インデックスを読み込む
    index_t_dict = dict()
    with open("index_t.txt", "r", encoding="utf-8") as f:
        for line in f:
            k, v = line.split("\t")
            index_t_dict[k] = int(v)
    return index_t_dict

if __name__ == "__main__":
    trg_word = "United_States"

    X_300 = load_matrix()
    index_t = load_index_t()

    # 対象の単語ベクトルを表示する
    print(X_300[index_t[trg_word]])
