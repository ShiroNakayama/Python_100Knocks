# 83. 単語／文脈の頻度の計測
# 82の出力を利用し，以下の出現分布，および定数を求めよ．
#
# ・f(t,c): 単語tと文脈語cの共起回数
# ・f(t,∗): 単語tの出現回数
# ・f(∗,c): 文脈語cの出現回数
# ・N: 単語と文脈語のペアの総出現回数


def count_co_occurrence_num(contexts, n, word_occurrence_num, context_word_occurrence_num):
    co_occurrence_num = dict()
    for pair in contexts:
        word, context_word = pair.split("\t")

        co_occurrence = f"{word}\t{context_word}"
        if co_occurrence in co_occurrence_num:
            co_occurrence_num[co_occurrence] += 1
        else:
            # メモリ節約のため、f(t,∗)とf(∗,c)が共に規定回数以下(=辞書から除外されていた)ならf(t,c)は無視する
            if word in word_occurrence_num or context_word in context_word_occurrence_num:
                co_occurrence_num[co_occurrence] = 1

    # メモリ節約のため、出現回数がn回に満たないデータは削除する
    del_list = []
    for k, v in co_occurrence_num.items():
        if v < n:
            del_list += [k]
    for w in del_list:
        del co_occurrence_num[w]

    return co_occurrence_num


def count_word_occurrence_num(contexts, n):
    word_occurrence_num = dict()
    for pair in contexts:
        word, context_word = pair.split("\t")

        if word in word_occurrence_num:
            word_occurrence_num[word] += 1
        else:
            word_occurrence_num[word] = 1

    # メモリ節約のため、出現回数がn回に満たないデータは削除する
    del_list = []
    for k, v in word_occurrence_num.items():
        if v < n:
            del_list += [k]
    for w in del_list:
        del word_occurrence_num[w]

    return word_occurrence_num


def count_context_word_occurrence_num(contexts, n):
    context_word_occurrence_num = dict()
    for pair in contexts:
        word, context_word = pair.split("\t")

        if context_word in context_word_occurrence_num:
            context_word_occurrence_num[context_word] += 1
        else:
            context_word_occurrence_num[context_word] = 1

    # メモリ節約のため、出現回数がn回に満たないデータは削除する
    del_list = []
    for k, v in context_word_occurrence_num.items():
        if v < n:
            del_list += [k]
    for w in del_list:
        del context_word_occurrence_num[w]

    return context_word_occurrence_num

if __name__ == "__main__":
    from chapter9 import ex82

    context_list = ex82.get_context()
    print(f"N: {len(context_list)}")
    t = count_word_occurrence_num(context_list, 10)
    print(len(t))
    c = count_context_word_occurrence_num(context_list, 10)
    print(len(c))
    print(len(count_co_occurrence_num(context_list, 10, t, c)))
