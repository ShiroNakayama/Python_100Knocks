# 93. アナロジータスクの正解率の計算
# 92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．


def calc_model_accuracy(file_name):
    enc = "utf-8"
    data_num = 0
    correct_num = 0
    with open(file_name, "r", encoding=enc) as f:
        for line in f:
            tmp = line.split(" ")
            if tmp[3] == tmp[4]:
                correct_num += 1
            data_num += 1

    return correct_num / data_num


if __name__ == "__main__":
    input_file_name1 = "family_with_similarity_ex90.txt"
    input_file_name2 = "family_with_similarity_ex85.txt"
    print("正解率")
    print(f"ex90: {calc_model_accuracy(input_file_name1)}")
    print(f"ex85: {calc_model_accuracy(input_file_name2)}")
