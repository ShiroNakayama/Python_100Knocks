# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
from chapter03.ex20 import extract_england
import re

contents = extract_england()
# カテゴリ名の書式　[[Category:カテゴリ名]]
# ?　非貪欲マッチの特殊文字（最小一致のマッチ）
# (...)　マッチ対象
# (?:...)　マッチ対象外
ptn = re.compile(r"\[\[Category:(.*?)(?:\]\]|\|)")

result = ptn.findall(contents)
for line in result:
    print(line)
