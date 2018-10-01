# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
import numpy as np

obj_file_name = "sentiment.txt"
enc = "utf-8"
# 入出力両方に使いたいので拡張子は省いておく
feature_file_name = "features"


def sigmoid(x):
    """
    シグモイド関数
    :param x: 入力値(numpyベクトル)
    :return: シグモイド関数の出力値
    """
    return 1 / (1 + np.exp(-x))


def load_feature():
    """
    素性ファイルを読み込む
    :return: 読み込んだ素性データの辞書
    """
    features_dict = dict()
    count = 1
    with open(feature_file_name + ".txt", "r", encoding=enc) as f:
        for line in f:
            features_dict[line[:-1]] = count
            count += 1
    return features_dict


def read_sentiment(file_name):
    """
    学習対象ファイルを読み込む
    :return: 読み込んだ学習対象文のリスト
    """
    sentiments = []
    with open(file_name, "r", encoding=enc) as f:
        for line in f:
            sentiments += [line]
    print("Read files: complete")
    return sentiments


def calc_params(features, sentiments, params, class_answer):
    """
    パラメータおよび正解データを学習対象ファイルから算出する
    :return:
    """
    import re
    from chapter08 import ex72
    ptn = re.compile(r"[,.\n\d-]+")
    for i, line in enumerate(sentiments):
        tag = line[:2]
        words = ptn.sub("", line[3:]).split(" ")
        words = ex72.remove_noise(words)
        # バイアス分は常に1
        params[i, 0] = 1
        for w in words:
            try:
                params[i, features[w]] = 1
            except KeyError:
                # 素性に無い単語があれば無視
                pass

        if tag == "+1":
            class_answer[i] = 1
    print("Set params: complete")


def training_with_gradient_descent(x, y, theta, eta, round_num):
    """
    ロジスティック回帰モデルの重みを最急降下法で学習する
    :param x: 特徴ベクトル
    :param y: 正解データ
    :param theta: 学習対象の重み
    :param eta: 学習係数
    :param round_num: 重みを更新する回数
    :return:
    """
    for cnt in range(round_num):
        p = x @ theta  # @: 行列積
        # パラメータ更新
        theta += eta * (y - sigmoid(p)) @ x
        if cnt % 100 == 0:
            print(f"Training: {cnt}times")
    print("Train weights: complete")


if __name__ == "__main__":
    # 素性と学習ファイルの読み込み
    features = load_feature()
    sentiments = read_sentiment(obj_file_name)

    # 各パラメータをベクトル化
    weights = np.zeros(len(features) + 1)
    class_answer = np.zeros(len(sentiments))
    params = np.zeros([len(class_answer), len(weights)])

    # パラメータおよび正解データを学習対象ファイルから算出する
    calc_params(features, sentiments, params, class_answer)

    # 重みを最急降下法で学習する
    training_with_gradient_descent(params, class_answer, weights, 0.01, 1000)

    # 学習結果を記録する
    with open(feature_file_name + "_with_weights.txt", "w", encoding=enc) as f:
        print(f"-,{weights[0]}", file=f)
        for k, v in sorted(features.items(),  key=lambda x: x[1]):
            print(f"{k},{weights[v]}", file=f)

    # 学習結果を表示する
    predicts = sigmoid(params @ weights)
    for ans, pred in zip(class_answer, predicts):
        print(f"{ans}: {pred}")

