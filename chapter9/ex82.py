# 82. 文脈の抽出
# 81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
# ただし，文脈語の定義は次の通りとする．
#
# ・ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
# ・単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
file_name = "corpus.txt"
enc = "utf-8"


def get_context():
    import random

    result = []
    with open(file_name, "r", encoding=enc) as f:
        # nbspでは単語を分けない方針とする
        words = f.read().split(" ")
        for i, w in enumerate(words):
            d = random.randint(1, 5)
            for n in range(max(0, i-d), min(len(words), i+d+1)):
                if n != i:
                    result += [f"{w}\t{words[n]}"]
    return result

if __name__ == "__main__":
    for line in get_context():
        print(line)
