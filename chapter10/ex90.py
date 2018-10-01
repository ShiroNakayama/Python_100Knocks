# 90. word2vecによる学習
# 81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
# さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
from gensim.models import word2vec  # pipからword2vecモジュールが入らなかったのでgensimモジュールから読み込む
from chapter9 import ex86, ex87, ex88
import numpy as np

model_file_name = "model"

sentences = word2vec.Text8Corpus("../chapter9/corpus.txt")
dimension = 300

# モデルを学習する（次元数は300で指定、出現回数が10回未満の単語は無視）
model = word2vec.Word2Vec(sentences, size=dimension, min_count=10)
model.save(model_file_name)
print(len(model.wv.vocab))

# 試しにモデルを動かしてみる
# results = model.wv.most_similar(positive=["England"])
# for result in results:
#     print(result)

# 学習したモデルをインデックスの順番でnumpyリストに変換する
index_t = dict()
count = 0
X_300 = np.zeros([len(model.wv.vocab), dimension])
for k, v in model.wv.vocab.items():
    try:
        index_t[k] = count
        X_300[count] += model.wv.word_vec(k)
        count += 1
        if count % 1000 == 0:
            print(f"translating: {count}")
    except KeyError:
        print(k)
print()

# 問題の意図はおそらく単語ベクトルファイル作成だが、容量を食うのでそのまま適用することとする
# ex86: 対象の単語ベクトルを表示する
print("<ex86>")
trg_word1 = "United_States"
ex86.print_vector(X_300, index_t[trg_word1])
print()

# ex87: 対象2単語のコサイン類似度を計算する
print("<ex87>")
trg_word2 = "U.S"
print(ex87.calc_cosine_similarity(X_300[index_t[trg_word1]], X_300[index_t[trg_word2]]))
print()

# ex88: 対象となる単語と類似度が高い10語を出力する
print("<ex88>")
trg_word3 = "England"
vector = X_300[index_t[trg_word3]]
print(ex88.get_similar_words(vector, 10, X_300, index_t))
print()

# ex89: 演算したベクトルと類似度が高い10語を出力する
print("<ex89>")
vector = X_300[index_t["Spain"]] - X_300[index_t["Madrid"]] + X_300[index_t["Athens"]]
print(ex88.get_similar_words(vector, 10, X_300, index_t))
