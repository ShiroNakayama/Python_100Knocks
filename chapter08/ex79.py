# 79. 適合率-再現率グラフの描画
# ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
import numpy as np
from chapter08 import ex73
import matplotlib.pyplot as plt

obj_file_name = "sentiment.txt"

# 素性と学習ファイルの読み込み
features = ex73.load_feature()
sentiments = ex73.read_sentiment(obj_file_name)

# 各パラメータをベクトル化
weights = np.zeros(len(features) + 1)
class_answer = np.zeros(len(sentiments))
params = np.zeros([len(class_answer), len(weights)])

# パラメータおよび正解データを学習対象ファイルから算出する
ex73.calc_params(features, sentiments, params, class_answer)

# 重みを最急降下法で学習する
# 学習係数を低めにして学習精度が低いうちに停止させる
ex73.training_with_gradient_descent(params, class_answer, weights, 0.001, 500)

# 学習結果を表示する
predicts = ex73.sigmoid(params @ weights)
precisions = []
recalls = []
for th in np.arange(0.0, 1.0, 0.01):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for ans, pred in zip(class_answer, predicts):
        if ans == 1:
            if pred >= th:
                true_positive += 1
            else:
                false_negative += 1
        elif ans == 0:
            if pred >= th:
                false_positive += 1
            else:
                true_negative += 1

    # 適合率を計算
    precision = true_positive / (true_positive + false_positive)
    precisions += [precision]

    # 再現率を計算
    recall = true_positive / (true_positive + false_negative)
    recalls += [recall]

# 適合率-再現率グラフを描画
plt.plot(precisions, recalls)
plt.grid()
plt.title("Precision-Recall Graph")
plt.xlabel("Precision")
plt.ylabel("Recall")

plt.show()
