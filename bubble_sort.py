# バブルソート 隣接要素を比較して、逆順なら交換することを繰り返す

list_a = [3, 4, 5, 6, 6, 7, 1, 4]
# i: 0 => list_aの長さ-1
for i in range(len(list_a)):
    # j: 0 => list_aの長さ -1 - i - 1
    # 1回のソートで配列の何番目まで行くか。
    # 1回目は右端、ソートする範囲を狭める
    for j in range(0, len(list_a) - i - 1):
        if list_a[j] > list_a[j+1]:
            list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

print(list_a)
