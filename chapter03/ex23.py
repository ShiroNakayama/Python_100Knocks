# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
from chapter03.ex20 import extract_england
import re

contents = extract_england()
# セクション名の書式　== セクション名 ==
# レベルが上がるほど=の数が増える
ptn = re.compile(r"(={2,})\s*(.+?)\s*={2,}")

result = ptn.findall(contents)
for line in result:
    # line[0]にはセクションのレベルが入っている
    level = len(line[0]) - 1
    print("Level: " + str(level) + ", Section: " + line[1])
