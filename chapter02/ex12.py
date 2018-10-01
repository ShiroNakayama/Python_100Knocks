# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
import chapter02.ex10 as func

f = func.read_file()
if f is not None:
    out1 = ""
    out2 = ""
    for line in f:
        words = line.split("\t")
        out1 += words[0] + "\n"
        out2 += words[1] + "\n"

    fout1 = open("col1.txt", "w", encoding='UTF-8')
    fout2 = open("col2.txt", "w", encoding='UTF-8')
    fout1.write(out1)
    fout2.write(out2)

    f.close()
