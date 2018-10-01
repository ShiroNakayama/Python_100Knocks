# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．


def read_mecab():
    file_name = "neko.txt.mecab"
    result = []

    # mecabの出力形式：
    # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    with open(file_name, encoding="utf-8") as m_data:
        for line in m_data:
            temp_dict = dict()
            parts = line.split(",")
            # 原形まで解析できていたら記録する
            # 読み、発音は無い場合がある
            # 例）ぷうぷうと	名詞,一般,*,*,*,*,*
            if len(parts) >= 7:
                # 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納
                temp_dict["surface"], temp_dict["pos"] = parts[0].split("\t")
                temp_dict["base"] = parts[6]
                temp_dict["pos1"] = parts[1]
                # 1文を形態素（マッピング型）のリストとして保存
                result += [temp_dict]
                if temp_dict["pos1"] == "句点":
                    yield result
                    result = []


if __name__ == "__main__":
    result_generator = read_mecab()
    for l in result_generator:
        print(l)

