# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
from chapter03.ex20 import extract_england
from chapter03.ex28 import remove_markups
from urllib import parse
from urllib import request
import json

result = remove_markups(extract_england())

url = "https://www.mediawiki.org/w/api.php?" \
    + "action=query" \
    + "&titles=File:" + parse.quote(result["国旗画像"]) \
    + "&format=json" \
    + "&prop=imageinfo" \
    + "&iiprop=url"

# MediaWikiへリクエスト送信
req = request.Request(url, headers={"User-Agent": "NLP100_Python(@segavvy)"})
connection = request.urlopen(req)

# jsonとして受信
data = json.loads(connection.read().decode())
# print(data)

# URL取り出し
image_info = data["query"]["pages"]["-1"]["imageinfo"]
# print(image_info)
result_url = image_info[0]["url"]

print(result_url)
