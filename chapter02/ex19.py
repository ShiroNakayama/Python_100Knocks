# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
import chapter02.ex10 as func

f = func.read_file()
if f is not None:
    # 各行の1列目の文字列の出現頻度を求める
    words_counter = dict()
    for line in f:
        word = line.split("\t")[0]
        try:
            # 既出の単語の場合はカウンタを進める
            words_counter[word] += 1
        except KeyError:
            # 初出の単語の場合はカウンタに1をセット
            words_counter[word] = 1

    # 各行の1列目の文字列の出現頻度を高い順に並べて表示
    for k, v in sorted(words_counter.items(), key=lambda x: x[1], reverse=True):
        print(v, k)
