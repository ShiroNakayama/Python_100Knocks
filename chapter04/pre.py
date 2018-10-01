# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．
import MeCab

org_file_name = "neko.txt"
trg_file_name = "neko.txt.mecab"

with open(org_file_name, encoding="utf-8") as f_in, \
        open(trg_file_name, "w", encoding="utf-8") as f_out:
    m = MeCab.Tagger()
    f_out.write(m.parse(f_in.read()))
