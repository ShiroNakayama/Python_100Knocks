# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
import chapter2.ex10 as func

f = func.read_file()
if f is not None:
    file_contents = []
    for line in f:
        words = line.split("\t")
        file_contents += [words]

    # 3コラム目の数値の昇順で整列
    file_contents.sort(key=lambda x: x[2])

    for line in file_contents:
        for word in line:
            print(word, end='\t')
