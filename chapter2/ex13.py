# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．
import sys

try:
    f1 = open(sys.argv[1], "r", encoding='UTF-8')
    f2 = open(sys.argv[2], "r", encoding='UTF-8')
    out_data = ""
    for s1, s2 in zip(f1, f2):
        out_data += s1[:-1] + "\t" + s2

    out = open("ex13out.txt", "w", encoding='UTF-8')
    out.write(out_data)

    f1.close()
    f2.close()
    out.close()

except IndexError:
    print("Usage: ex13.py <filename1> <filename2>")

except FileNotFoundError:
    print("File not found: " + sys.argv[1] + ", " + sys.argv[2])