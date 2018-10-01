# 70. データの入手・整形
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
#
# 1．rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# 2．rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
import random

pos_file_name = "rt-polaritydata/rt-polarity.pos"
neg_file_name = "rt-polaritydata/rt-polarity.neg"
output_file_name = "sentiment.txt"
input_enc = "cp1252"
output_enc = "utf-8"

pos = []
neg = []

# 1．pos_fileの各行の先頭に"+1 "という文字列を追加する
with open(pos_file_name, "r", encoding=input_enc) as f:
    for line in f:
        pos += ["+1 " + line]

# 2．neg_fileの各行の先頭に"-1 "という文字列を追加する
with open(neg_file_name, "r", encoding=input_enc) as f:
    for line in f:
        neg += ["-1 " + line]

# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
concatenated = pos + neg
random.shuffle(concatenated)

# sentiment.txtを作成する
with open(output_file_name, "w", encoding=output_enc) as f:
    for line in concatenated:
        f.write(line)

# 正例（肯定的な文）の数と負例（否定的な文）の数を確認
pos_cnt = 0
neg_cnt = 0
with open(output_file_name, "r", encoding=output_enc) as f:
    for line in f:
        tag = line[:2]
        if tag == "+1":
            pos_cnt += 1
        elif tag == "-1":
            neg_cnt += 1

print(f"正例（肯定的な文）：{pos_cnt}\n負例（否定的な文）：{neg_cnt}")
