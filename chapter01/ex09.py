# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば
# "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．


def typoglycemia(string):
    import random
    word_list = string.split(" ")
    result = ""
    for w in word_list:
        if len(w) > 4:
            random_str = list(w[1:-1])
            random.shuffle(random_str)
            new_w = w[0]
            for c in random_str:
                new_w += c
            new_w += w[-1]
            w = new_w
        result += w + " "

    return result


if __name__ == "__main__":
    test_string = "I couldn't believe that I could actually understand what I was reading : " \
             "the phenomenal power of the human mind ."
    print(typoglycemia(test_string))
