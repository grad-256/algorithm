# シェルソート 挿入ソートを改良したのも
# 等間隔で離れた要素同士を一つのグループとし、グループ内で挿入ソートを行う
# 最後に間隔を１にして完全に整列させる

def shellsort(data):
    gaps = [7, 3, 1]  # ギャップの値を設定
    for gap in gaps:  # ギャップを徐々に狭めて繰り返す
        for start in range(gap):  # ギャップ分離れた複数の組みを順番にソート
            for i in range(start, len(data), gap):  # ギャップの幅で飛ばしながら挿入ソート
                # print(start)
                # print(gap)
                for j in range(i-gap, -1, -gap):  # 終了値を−１に設定（０まで実行）
                    if data[j] > data[j+gap]:  # ギャップ分離れた要素で前の方が大きい場合
                        data[j], data[j+gap] = data[j+gap], data[j]  # 要素を入れ替える
                    else:
                        break  # 挿入する部分が見つかれば終わり
    return data  # 結果をreturnする


list_a = [15, 1, 2, 3, 7, 8, 9, 4, 5, 6, 7, 8, 9]

print(shellsort(list_a))
