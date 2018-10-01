# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．
from chapter03.ex20 import extract_england
import re

contents = extract_england()
# カテゴリ名の書式　[[Category:カテゴリ名]]
ptn = re.compile(r"\[\[Category:.*\]\]")

result = ptn.findall(contents)
for line in result:
    print(line)
