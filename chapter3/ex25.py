# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
from chapter3.ex20 import extract_england
import re

contents = extract_england()

# 基礎情報の書式　{{基礎情報 |フィールド名 = 値 | ... }}
ptn = re.compile(r"^{{基礎情報.*?$(.*?)^}}$", re.MULTILINE + re.DOTALL)

# 改行 + |で分離して一旦リストに保存
result = ptn.findall(contents)
fields = result[0].split("\n|")

# =の前後で分離して辞書として保存
fields = fields[1:]
standard_info = dict()
for f in fields:
    params = f.split(" = ")
    standard_info[params[0]] = params[1]

for k, v in sorted(standard_info.items()):
    print(k + ": " + v)
