# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
import chapter02.ex10 as func

f = func.read_file()
if f is not None:
    try:
        head = int(input("表示行数を入力 >"))
        for line, n in zip(f, range(head)):
            print(line, end="")
    except ValueError:
        print("数値を入力してください")

    f.close()

