# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
import chapter2.ex10 as func

f = func.read_file()
if f is not None:
    try:
        cnt = func.count_lines(f)
        tail = int(input("表示行数を入力 >"))
        f.seek(0)
        for line in f:
            if tail >= cnt:
                print(line, end="")
            tail += 1
    except ValueError:
        print("数値を入力してください")

    f.close()


