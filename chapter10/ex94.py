# 94. WordSimilarity-353での類似度計算
# The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，
# 各行の末尾に類似度の値を追加するプログラムを作成せよ．
# このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
import pandas as pd
from gensim.models import word2vec
from chapter09 import ex86, ex87

input_file_name = "wordsim353/combined.csv"
output_file_name1 = "combined_ex90.csv"
output_file_name2 = "combined_ex85.csv"

df = pd.read_csv(input_file_name)

# ex90の学習モデル
model = word2vec.Word2Vec.load("model")

# ex85の単語文脈行列
X_300 = ex86.load_matrix("../chapter09/word_context_matrix_dim300")
index_t = ex86.load_index_t("../chapter09/index_t.txt")

similarities_ex90 = []
similarities_ex85 = []
for w1, w2 in zip(df["Word 1"], df["Word 2"]):
    # ex90の類似度を計算
    try:
        similarities_ex90 += [model.wv.similarity(w1, w2)]
    except KeyError:
        # 対象の単語がモデルに無い場合
        similarities_ex90 += [0]

    # ex85の類似度を計算
    try:
        similarities_ex85 += [ex87.calc_cosine_similarity(X_300[index_t[w1]], X_300[index_t[w2]])]
    except KeyError:
        # 対象の単語がモデルに無い場合
        similarities_ex85 += [0]

# 求めた単語と類似度を追加して出力ファイルに書き込む
df.assign(similarity=similarities_ex90).to_csv(output_file_name1, index=None)
df.assign(similarity=similarities_ex85).to_csv(output_file_name2, index=None)

