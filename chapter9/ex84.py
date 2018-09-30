# 84. 単語文脈行列の作成
# 83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．
#
# f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{log(N×f(t,c)/(f(t,∗)×f(∗,c))),0}
# f(t,c)<10ならば，Xtc=0
# ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
# なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
# 幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
from chapter9 import ex82, ex83
from scipy import sparse, io
from collections import OrderedDict
import math

contexts = ex82.get_context()
threshold = 10

# 共起回数および出現回数を計測する
f_t = ex83.count_word_occurrence_num(contexts, threshold)
f_c = ex83.count_context_word_occurrence_num(contexts, threshold)
f_tc = ex83.count_co_occurrence_num(contexts, threshold, f_t, f_c)
print("count occurrences: finished")

# 単語文脈行列Xを準備する
index_t = OrderedDict((key, i) for i, key in enumerate(f_t.keys()))
index_c = OrderedDict((key, i) for i, key in enumerate(f_c.keys()))
X = sparse.lil_matrix((len(index_t), len(index_c)))

# 共起回数からPPMIを計算する
for k, v in f_tc.items():
    try:
        word, context_word = k.split("\t")
        # 非0の要素だけを書き出す
        if v >= threshold:
            ppmi = math.log(len(contexts) * v / f_t[word] / f_c[context_word])
            if ppmi > 0:
                X[index_t[word], index_c[context_word]] = ppmi
    except ValueError:
        print(k, v)
print("make X: finished")

# 単語文脈行列を書き出す
io.savemat("word_context_matrix", {"X": X})

# インデックスを保存する
# 確認がしやすいテキスト形式で保存する
with open("index_t.txt", "w", encoding="utf-8") as f:
    for k, v in index_t.items():
        print(f"{k}\t{v}", file=f)

# こちらは後の主成分分析で圧縮されてしまうため不要
# with open("index_c.txt", "w", encoding="utf-8") as f:
#     for k, v in index_c.items():
#         print(f"{k}\t{v}", file=f)
print("output files: finished")
