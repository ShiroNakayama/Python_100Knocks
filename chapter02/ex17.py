# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
import chapter02.ex10 as func

f = func.read_file()
if f is not None:
    # 1列目の文字列を集合に追加
    uniq = set()
    for line in f:
        words = line.split("\t")
        uniq.add(words[0])

    # 出力
    for s in sorted(uniq):
        print(s)
