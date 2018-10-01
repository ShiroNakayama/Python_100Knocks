# 91. アナロジーデータの準備
# 単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．
# 例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．
# ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
input_file_name = "questions-words.txt"
output_file_name = "family.txt"
enc = "utf-8"

with open(input_file_name, "r", encoding=enc) as in_f,\
        open(output_file_name, "w", encoding=enc) as out_f:
    is_trg_section = False
    for line in in_f:
        if is_trg_section:
            if line.startswith(": "):
                # 次のセクションを見つけたら終了
                break
            out_f.write(line)
        elif line.startswith(": family"):
            is_trg_section = True

