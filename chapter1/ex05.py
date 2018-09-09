# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def make_n_gram(seq, n):
    n_gram_list = []
    for i in range(len(seq) - (n-1)):
        n_gram = []
        for j in range(n):
            n_gram += [seq[i + j]]
        n_gram_list += [n_gram]
    return n_gram_list


def make_word_n_gram(seq, n):
    import re
    word_list = re.sub(r"[^a-zA-Z0-9 ]", "", seq).split(" ")
    return make_n_gram(word_list, n)


def make_char_n_gram(seq, n):
    import re
    characters = re.sub(r"[^a-zA-Z0-9]", "", seq)
    return make_n_gram(characters, n)


if __name__ == "__main__":
    string = "I am an NLPer"
    print(make_word_n_gram(string, 2))
    print(make_char_n_gram(string, 2))
