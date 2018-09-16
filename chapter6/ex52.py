# 52. ステミング
# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
# Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
from chapter6 import ex51
from nltk.stem.porter import PorterStemmer as PS

words = ex51.separate_words()
ps = PS()

for w in words:
    print(w + "\t" + ps.stem(w))
