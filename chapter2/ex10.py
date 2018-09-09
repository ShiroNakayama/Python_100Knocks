# -*- coding: utf-8 -*-
# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．


def read_file():
    import sys
    filename = ""
    try:
        filename = sys.argv[1]
        return open(filename, "r", encoding='UTF-8')

    except IndexError:
        print("Usage: ex10.py <filename>")

    except FileNotFoundError:
        print("File not found: " + filename)


def count_lines(file):
    # sum(1 for line in open('filename'))
    cnt = 0
    for line in file:
        cnt += 1
    return cnt


if __name__ == "__main__":
    f = read_file()
    if f is not None:
        print(count_lines(f))
        f.close()
