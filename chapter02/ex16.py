# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
import chapter02.ex10 as func

f = func.read_file()
if f is not None:
    try:
        import math
        cnt = func.count_lines(f)
        split_num = int(input("分割数を入力 >"))
        section_lines = math.ceil(cnt / split_num)

        f.seek(0)  # count_filesで最後尾まで動いたファイルオブジェクトの位置を先頭に戻す

        for n in range(1, split_num + 1):
            print(str(n) + "：")
            for line_num, line in zip(range(section_lines), f):
                print(line, end="")
            print()
    except ValueError:
        print("数値を入力してください")

    f.close()
