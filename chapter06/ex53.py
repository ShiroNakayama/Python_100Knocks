# 53. Tokenization
# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
import xml.etree.ElementTree as ET

file_name = "nlp.txt.xml"
# 解析結果のxmlをパース
root = ET.parse(file_name)

# wordのみ取り出し
for word in root.iter("word"):
    print(word.text)
