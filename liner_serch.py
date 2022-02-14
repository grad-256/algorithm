# 線形探索 番兵法

list_a = [3, 10, 4, 5, 6, 6, 7, 1, 4]

# 探したい値
search = 10
# 番兵
list_a.append(search)

# Linear search
# 目当ての値が見つかるまで配列の先頭から順に探索しつづけ、見つかったら終了
# 配列の一番最後に番兵をセットし必ずループが終わるようにする


def lin_search(tgt: int, lst: list):
    for i in range(len(lst)):
        if lst[i] == tgt:
            lst.pop()
            # return i + 1
            return i
    # 見つからなかたら-1を変えす
    return -1


res = lin_search(search, list_a)
print(res)
