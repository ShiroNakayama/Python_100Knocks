# 75. 素性の重み
# 73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
classifier_file_name = "features_with_weights.txt"
enc = "utf-8"

# 素性と重みの読み込み
features = dict()
with open(classifier_file_name, "r", encoding=enc) as f:
    for line in f:
        tmp = line[:-1].split(",")
        features[tmp[0]] = float(tmp[1])

# 重みの高い素性トップ10
ordered_feature = sorted(features.items(), key=lambda x: x[1])
print("top 10")
for item in ordered_feature[-1:-11:-1]:
    print(item)
print()

# 重みの低い素性トップ10
print("bottom 10")
for item in ordered_feature[:10]:
    print(item)
