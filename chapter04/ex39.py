# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from chapter04 import ex36

word_frequency = ex36.count_words()
# 出現頻度だけをリストにする
freq = [t[1] for t in word_frequency]

# グラフで日本が使えるように設定
fp = FontProperties(fname="C:\\WINDOWS\\Fonts\\MSGOTHIC.TTC", size=14)

# 散布図を作成
plt.scatter(range(1, len(word_frequency) + 1), freq)

# 両軸とも対数グラフにする
plt.xscale('log')
plt.yscale('log')

# 整形
plt.title("ex39. Zipf")
plt.xlabel("出現頻度順位", fontproperties=fp)
plt.ylabel("出現頻度", fontproperties=fp)
plt.grid(axis="y")

# 表示
plt.show()
