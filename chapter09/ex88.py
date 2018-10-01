# 88. 類似度の高い単語10件
# 85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
import numpy as np


def get_similar_words(trg_vector, num, matrix, matrix_index):
    """
    類似度の高い単語を抽出する
    :param trg_vector: 比較対象となる単語ベクトル
    :param num: 抽出する数
    :param matrix: 単語文脈行列
    :param matrix_index: 単語文脈行列のインデックス
    :return: 単語をキー、類似度を値にとる辞書（サイズ: num）
    """
    from chapter09 import ex87

    cosine_similarities = []
    for i in range(len(matrix_index)):
        cosine_similarity = ex87.calc_cosine_similarity(trg_vector, matrix[i])
        cosine_similarities += [cosine_similarity]

    # 類似度が高いnum個の単語を保存する
    sorted_index = np.argsort(cosine_similarities)
    t_words = list(matrix_index.keys())
    result_dict = dict()
    count = 0
    for i in sorted_index[-1::-1]:
        # 対象の単語は省く
        if cosine_similarities[i] < 0.9999:
            result_dict[t_words[i]] = cosine_similarities[i]
            count += 1
            if count >= num:
                break

    return result_dict


if __name__ == "__main__":
    from chapter09 import ex86
    # 単語文脈行列を読み込む
    X_300 = ex86.load_matrix("word_context_matrix_dim300")
    index_t = ex86.load_index_t("index_t.txt")

    # 対象となる単語と類似度が高い10語を出力する
    vector = X_300[index_t["England"]]
    print(get_similar_words(vector, 10, X_300, index_t))
