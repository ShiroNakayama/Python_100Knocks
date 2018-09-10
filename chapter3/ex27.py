# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ．
# （参考: https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8）
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

# 強調マークアップ書式　''他との区別'' or '''強調''' or '''''斜体と強調'''''
emphasis_ptn = re.compile(r"'{2,5}")
# 内部リンクの書式　[[記事名(#節名)(|表示文字)]]
inner_link_ptn = re.compile(r"\[\[(.+?)(?:#.*)*(?:\|.*)*]]")

for f in fields:
    f = emphasis_ptn.sub("", f)  # 強調マークアップを除去
    f = inner_link_ptn.sub(r"\1", f)  # 内部リンクを除去

    params = f.split(" = ")
    standard_info[params[0]] = params[1]

for k, v in sorted(standard_info.items()):
    print(k + ": " + v)
