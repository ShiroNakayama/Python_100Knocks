# 76. ラベル付け
# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
import numpy as np
import sys
import re
from chapter08 import ex72, ex73


def apply_classifier_with_ground_truth(file_name):
    classifier_file_name = "features_with_weights.txt"
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
    sentiments = ex73.read_sentiment(file_name)

    # 各パラメータをベクトル化
    weights = np.array(weight_list)
    class_answer = np.zeros(len(sentiments))
    params = np.zeros([len(class_answer), len(weights)])

    # パラメータおよび正解データを学習対象ファイルから算出する
    ex73.calc_params(features, sentiments, params, class_answer)

    # 学習結果を表示する
    # 与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を表示する
    predicts = ex73.sigmoid(params @ weights)
    output = ""
    for ans, pred in zip(class_answer, predicts):
        # 正解ラベル
        if ans == 0:
            output += "-1\t"
        else:
            output += "+1\t"

        # 予測されたラベル
        if pred < 0.5:
            output += "-1\t"
        else:
            output += "+1\t"

        # 予測確率
        output += str(pred) + "\n"
    return output

if __name__ == "__main__":
    try:
        # 読み込みファイルを引数で指定する
        # sentiment.txtを指定
        sentiment_file_name = sys.argv[1]
        print(apply_classifier_with_ground_truth(sentiment_file_name))
    except IndexError:
        print("入力ファイルを指定してください")
