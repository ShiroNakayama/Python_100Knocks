# 81. 複合語からなる国名への対処
# 英語では，複数の語の連接が意味を成すことがある．
# 例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，
# "United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．
# そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．
# しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．
#
# インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．
# 例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
country_file_name = "countries.txt"
input_file_name = "corpus_raw.txt"
output_file_name = "corpus.txt"
enc = "utf-8"

# 国名を読み込み、辞書に登録する。
# 1単語目をキーとし、全体をリストにして保存しておく
countries = dict()
with open(country_file_name, "r", encoding=enc) as f:
    for line in f:
        words = line.strip("\n").split(" ")
        if len(words) > 1:
            # 2単語以上で構成されていたら辞書に登録する
            if words[0] in countries:
                countries[words[0]] += [words]
            else:
                countries[words[0]] = [words]

# ex80で作成したファイルを読み込み、国名をまとめる
tokens = []
with open(input_file_name, "r", encoding=enc) as f:
    words = f.read().split(" ")
    ignore_num = 0
    for i, w in enumerate(words):
        if ignore_num > 0:
            # すでに連結した単語だったら無視
            ignore_num -= 1
        else:
            if w in countries:
                # 複数文字で構成される国名の1単語目を見つけた場合
                check_num = 0
                for country in countries[w]:
                    count = 0
                    for n, c_word in enumerate(country):
                        # 国名の各単語について、合っていた数を数える
                        if c_word == words[i + n]:
                            count += 1
                        else:
                            break

                    if count == len(country):
                        # 全単語が合ったら"_"でつなげて登録する
                        tokens += ["_".join(country)]
                        ignore_num = len(country) - 1
                        break
                    else:
                        # 合っていなければ調査数を増やして継続
                        check_num += 1

                if check_num == len(countries[w]):
                    # 国名ではなかった場合
                    tokens += [w]
            else:
                # 複数単語で構成される国名ではなかった場合
                tokens += [w]

# ファイルに出力する
with open(output_file_name, "w", encoding=enc) as f:
    print(*tokens, sep=" ", end="", file=f)
