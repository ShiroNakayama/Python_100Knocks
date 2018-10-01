# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from chapter04 import ex36

word_frequency = ex36.count_words()
# 出現頻度が高い10語を抽出
size = 10
word_frequency = word_frequency[:size]
left = []
height = []
for t in word_frequency:
    left += [t[0]]
    height += [t[1]]

# グラフで日本が使えるように設定
fp = FontProperties(fname="C:\\WINDOWS\\Fonts\\MSGOTHIC.TTC", size=14)

# 一旦整数値を横軸にとる
plt.bar(range(size), height)

# 整数値に対応したラベルを日本語で付ける
plt.xticks(range(size), left, fontproperties=fp)

# 整形
plt.title("ex37. Words frequency")
plt.xlabel("単語", fontproperties=fp)
plt.ylabel("出現頻度", fontproperties=fp)
plt.grid(axis="y")

# 表示
plt.show()
