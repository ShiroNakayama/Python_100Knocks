# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
import chapter02.ex10 as func

f = func.read_file()
if f is not None:
    data = f.read()
    replaced = data.replace("\t", " ")
    print(replaced)

    f.close()
