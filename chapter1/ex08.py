# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#     ・英小文字ならば(219 - 文字コード)の文字に置換
#     ・その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(string):
    ciphered = ""
    a_code = ord("a")
    z_code = ord("z")
    for c in string:
        code = ord(c)
        if a_code <= code <= z_code:
            ciphered += chr(219 - code)
        else:
            ciphered += c

    return ciphered


if __name__ == "__main__":
    org = "I have a pen."
    cip_str = cipher(org)
    print(cip_str)
    print(cipher(cip_str))
