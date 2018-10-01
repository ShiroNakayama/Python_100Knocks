# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
from chapter03.ex20 import extract_england
import re

contents = extract_england()
# メディアファイルの書式　File:メディアファイル名|... または ファイル:メディアファイル名|...
ptn = re.compile(r"(?:File|ファイル):(.+?)\|")

result = ptn.findall(contents)
for line in result:
    print(line)
