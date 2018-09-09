# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去して
# テキストに変換せよ（参考: https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8）．
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
del_ptn = re.compile(r"'{2,5}")  # ex26追加
for f in fields:
    # 強調マークアップを除去
    f = del_ptn.sub("", f)  # ex26追加
    params = f.split(" = ")
    standard_info[params[0]] = params[1]

for k, v in sorted(standard_info.items()):
    print(k + ": " + v)

