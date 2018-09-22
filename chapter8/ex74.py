# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，
# 与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
import numpy as np
import sys
import re
from chapter8 import ex72, ex73

classifier_file_name = "features_with_weights.txt"
try:
    # 読み込みファイルを引数で指定する
    # unknown_reviews.txtを指定した場合、正解は+1, -1, -1。
    sentiment_file_name = sys.argv[1]
except IndexError:
    print("入力ファイルを指定してください")
    exit(1)
enc = "utf-8"

# 素性と重みの読み込み
features = dict()
weight_list = []
count = 0
with open(classifier_file_name, "r", encoding=enc) as f:
    for line in f:
        tmp = line[:-1].split(",")
        features[tmp[0]] = count
        weight_list += [float(tmp[1])]
        count += 1

# 予測対象ファイルの読み込み
sentiments = ex73.read_sentiment(sentiment_file_name)

# 各パラメータをベクトル化
weights = np.array(weight_list)
class_answer = np.zeros(len(sentiments))
params = np.zeros([len(class_answer), len(weights)])

# パラメータおよび正解データを学習対象ファイルから算出する
ptn = re.compile(r"[,.\n\d-]+")
for i, line in enumerate(sentiments):
    words = ptn.sub("", line).split(" ")
    words = ex72.remove_noise(words)
    # バイアス分は常に1
    params[i, 0] = 1
    for w in words:
        try:
            params[i, features[w]] = 1
        except KeyError:
            # 素性に無い単語があれば無視
            pass
print("Set params: complete")

# 学習結果を表示する
# 与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を表示する
predicts = ex73.sigmoid(params @ weights)
for pred in predicts:
    output = ""
    if pred < 0.5:
        output += "-1: "
    else:
        output += "+1: "

    output += str(pred)
    print(output)
