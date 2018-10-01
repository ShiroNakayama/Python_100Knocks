# 86. 単語ベクトルの表示
# 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
# ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
from scipy import io


def load_matrix(file_name):
    """
    単語文脈行列とそのインデックスを読み込む
    :return: 単位文脈行列(疎行列）
    """
    return io.loadmat(file_name)["X_300"]


def load_index_t(file_name):
    # インデックスを読み込む
    index_t_dict = dict()
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            k, v = line.split("\t")
            index_t_dict[k] = int(v)
    return index_t_dict


def print_vector(matrix, index):
    print(matrix[index])


if __name__ == "__main__":
    trg_word = "United_States"

    X_300 = load_matrix("word_context_matrix_dim300")
    index_t = load_index_t("index_t.txt")

    # 対象の単語ベクトルを表示する
    print_vector(X_300, index_t[trg_word])
    print(type(X_300))
