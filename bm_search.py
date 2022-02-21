# BM法 ボイヤームーア なるべく多くずらすことで比較回数を減らす
# 文字列探索


def search(text, pattern):
    skip_dic = dict()  # スキップ数（辞書形式）の作成
    for i, character in enumerate(pattern):
        # enumerate 関数の引数にリストなどのイテラブルオブジェクトを指定
        # イテラブルオブジェクトとは、文字列、リスト、タプルなどのように要素を順番に取り出せるオブジェクト
        skip_dic[character] = len(pattern) - i
    i = 0  # 文字の比較
    while i < len(text) - len(pattern):
        for j in range(len(pattern)):
            if text[i+j] == pattern[j]:
                if j == len(pattern) - 1:
                    return i
            else:
                break
        if text[i+len(pattern)-1] not in skip_dic:  # スキップ数の決定
            skip = len(pattern)
        else:
            skip = skip_dic[text[i+len(pattern)-1]]
        i += skip
    return -1


pattern = "h"
data = search("探索する文字列の中にhogeがあります", pattern)
print("探索文字が見つかった位置: {}.".format(data))
