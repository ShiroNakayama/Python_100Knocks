# 78. 5分割交差検定
# 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
# すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
# そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
import numpy as np
from chapter8 import ex73

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

# パラメータおよび正解データを分割する
sep_num = 5
sep_params = np.array_split(params, sep_num)
sep_class_answer = np.array_split(class_answer, sep_num)

# 交差検定
accuracies = []
precisions = []
recalls = []
f1_scores = []
for validate_id in range(sep_num):
    print(f"{validate_id + 1}/{sep_num}")

    # 学習データと検証データを決める
    train_params = None
    train_class_answer = None
    for i in range(sep_num):
        if i == validate_id:
            validate_params = sep_params[i]
            validate_class_answer = sep_class_answer[i]
        else:
            if train_params is None:
                train_params = sep_params[i]
                train_class_answer = sep_class_answer[i]
            else:
                np.concatenate((train_params, sep_params[i]), axis=0)
                np.concatenate((train_class_answer, sep_class_answer[i]), axis=0)

    # 重みを最急降下法で学習する
    ex73.training_with_gradient_descent(train_params, train_class_answer, weights, 0.01, 1000)

    # 学習結果を適用し、正解率，適合率，再現率，F1スコアを求める
    predicts = ex73.sigmoid(validate_params @ weights)
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for ans, pred in zip(validate_class_answer, predicts):
        if ans == 1:
            if pred >= 0.5:
                true_positive += 1
            else:
                false_negative += 1
        elif ans == 0:
            if pred >= 0.5:
                false_positive += 1
            else:
                true_negative += 1

    print("\t\t| pos\t| neg ")
    print(f"pre-pos\t| {true_positive}\t| {false_positive}")
    print(f"pre-neg\t| {false_negative}\t| {true_negative}")

    # 正解率を計算
    accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)
    accuracies += [accuracy]

    # 適合率を計算
    precision = true_positive / (true_positive + false_positive)
    precisions += [precision]

    # 再現率を計算
    recall = true_positive / (true_positive + false_negative)
    recalls += [recall]

    # F1スコアを計算
    f1_score = 2 / (1 / precision + 1 / recall)
    f1_scores += [f1_score]

    print()
    print(f"Accuracy {validate_id}: {accuracy}")
    print(f"Precision {validate_id}: {precision}")
    print(f"Recall {validate_id}: {recall}")
    print(f"F1 Score {validate_id}: {f1_score}")
    print()

print("Total result...")
print(f"Accuracy {validate_id}: {np.average(accuracies)}")
print(f"Precision {validate_id}: {np.average(precisions)}")
print(f"Recall {validate_id}: {np.average(recalls)}")
print(f"F1 Score {validate_id}: {np.average(f1_scores)}")
