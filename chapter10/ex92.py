# 92. アナロジーデータへの適用
# 91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
# そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
# このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
from gensim.models import word2vec
from chapter09 import ex86, ex88

input_file_name = "family.txt"
output_file_name1 = "family_with_similarity_ex90.txt"
output_file_name2 = "family_with_similarity_ex85.txt"
enc = "utf-8"

# ex90の学習モデル
model = word2vec.Word2Vec.load("model")

# ex85の単語文脈行列
X_300 = ex86.load_matrix("../chapter09/word_context_matrix_dim300")
index_t = ex86.load_index_t("../chapter09/index_t.txt")

with open(input_file_name, "r", encoding=enc) as in_f, \
        open(output_file_name1, "w", encoding=enc) as out_f1, \
        open(output_file_name2, "w", encoding=enc) as out_f2:
    for line in in_f:
        line = line.strip("\n")
        tmp = line.split(" ")

        # ex90の類似度を計算
        try:
            # vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)
            trg_vec = model.wv.word_vec(tmp[1]) - model.wv.word_vec(tmp[0]) + model.wv.word_vec(tmp[2])
            word, similarity = model.wv.similar_by_vector(trg_vec, topn=1)[0]
        except KeyError:
            # 対象の単語がモデルに無い場合
            word = "-"
            similarity = 0
        # 求めた単語と類似度を追加して出力ファイルに書き込む
        print(f"{line} {word} {similarity}", file=out_f1)

        # ex85の類似度を計算
        try:
            # vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)
            trg_vec = X_300[index_t[tmp[1]]] - X_300[index_t[tmp[0]]] + X_300[index_t[tmp[2]]]
            ret_dict = ex88.get_similar_words(trg_vec, 1, X_300, index_t)
            word = list(ret_dict)[0]
            similarity = ret_dict[word]
        except KeyError:
            # 対象の単語がモデルに無い場合
            word = "-"
            similarity = 0
        # 求めた単語と類似度を追加して出力ファイルに書き込む
        print(f"{line} {word} {similarity}", file=out_f2)
