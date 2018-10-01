# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
# さらに，その関数に対するテストを記述せよ．
from nltk.corpus import stopwords
stop_words_list = stopwords.words("english")


def is_stop_word(word):
    return word.lower() in stop_words_list

if __name__ == "__main__":
    test_str = "I have a pen and you can use it"
    for w in test_str.split(" "):
        print(w + ": ", is_stop_word(w))

