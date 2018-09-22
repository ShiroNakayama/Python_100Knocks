# 77. 正解率の計測
# 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
from chapter8 import ex76

sentiment_file_name = "sentiment.txt"
output = ex76.apply_classifier_with_ground_truth(sentiment_file_name)

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0
for line in output.split("\n"):
    tmp = line.split("\t")
    if tmp[0] == "+1":
        if tmp[1] == "+1":
            true_positive += 1
        elif tmp[1] == "-1":
            false_negative += 1
    elif tmp[0] == "-1":
        if tmp[1] == "+1":
            false_positive += 1
        elif tmp[1] == "-1":
            true_negative += 1

print("\t\t| pos\t| neg ")
print(f"pre-pos\t| {true_positive}\t| {false_positive}")
print(f"pre-neg\t| {false_negative}\t| {true_negative}")

# 正解率を計算
accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)

# 適合率を計算
precision = true_positive / (true_positive + false_positive)

# 再現率を計算
recall = true_positive / (true_positive + false_negative)

# F1スコアを計算
f1_score = 2 / (1 / precision + 1 / recall)

print()
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1_score}")
