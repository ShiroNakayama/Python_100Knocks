# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
# 国の基本情報を整形せよ．


def remove_markups(contents):
    import re
    # 基礎情報の書式　{{基礎情報 |フィールド名 = 値 | ... }}
    ptn = re.compile(r"^{{基礎情報.*?$(.*?)^}}$", re.MULTILINE + re.DOTALL)

    # 改行 + |で分離して一旦リストに保存
    result = ptn.findall(contents)
    fields = result[0].split("\n|")

    # =の前後で分離して辞書として保存
    fields = fields[1:]
    standard_info = dict()

    # 強調マークアップ書式　''他との区別'' or '''強調''' or '''''斜体と強調'''''
    emphasis_ptn = re.compile(r"'{2,5}")
    # 内部リンクの書式　[[記事名(#節名)(|表示文字)]]
    inner_link_ptn = re.compile(r"\[\[(.+?)(?:#.*)*(?:\|.*)*]]")
    # そのほかのマークアップ言語の除去
    # Lang書式　{{lang|言語|文字列}}
    lang_ptn = re.compile(r"{{lang\|.*?\|(.*?)}}")
    # 外部リンク書式 [http://www.example.org 表示文字]
    outer_link_ptn = re.compile(r"\[(?:.*?\s)(.*?)]")
    # その他：<br><ref><references />
    markup_other_ptn = re.compile(r"</?.*?>")

    for f in fields:
        f = emphasis_ptn.sub("", f)  # 強調マークアップを除去
        f = inner_link_ptn.sub(r"\1", f)  # 内部リンクを除去
        f = lang_ptn.sub(r"\1", f)  # Lang書式を除去
        f = outer_link_ptn.sub(r"\1", f)  # 外部リンクを除去
        f = markup_other_ptn.sub("", f)  # <br><ref><references />の除去

        params = f.split(" = ")
        standard_info[params[0]] = params[1]

    return standard_info

if __name__ == "__main__":
    from chapter03.ex20 import extract_england
    result = remove_markups(extract_england())

    for k, v in sorted(result.items()):
        print(k + ": " + v)

