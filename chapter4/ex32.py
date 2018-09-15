# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．
from chapter4 import ex31

verbs_base = [verb["base"] for verb in ex31.extract_verbs()]

print(verbs_base)
