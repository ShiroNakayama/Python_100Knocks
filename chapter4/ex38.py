# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from chapter4 import ex36

word_frequency = ex36.count_words()
# 出現頻度だけをリストにする
freq = [t[1] for t in word_frequency]

# グラフで日本が使えるように設定
fp = FontProperties(fname="C:\\WINDOWS\\Fonts\\MSGOTHIC.TTC", size=14)

# ヒストグラム作成
plt.hist(freq, bins=50, range=(1, 50))
# x軸の値の範囲の調整（デフォルトだと0が入る）
plt.xlim(xmin=1, xmax=50)

# 整形
plt.title("ex38. Words histogram")
plt.xlabel("出現頻度", fontproperties=fp)
plt.ylabel("出現頻度をとる単語の種類数", fontproperties=fp)
plt.grid(axis="y")

# 表示
plt.show()
