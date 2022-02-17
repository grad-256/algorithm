# 二分探索 昇順降順といった規則性を持つデータ場合有効
# ソートをあらかじめを行う必要がある
# middleとは中央の意
import numbers


list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
search_value = 40


def binary_search(data: numbers, value: numbers):
    # 探索する範囲の左端を設定
    left = 0
    # 探索する範囲の右端を設定
    right = len(data) - 1
    while left <= right:
        # 探索する範囲の中央を計算
        # //2は整数除算
        middle = (left + right)//2
        if data[middle] == value:
            # 中央の値と一致した場合は位置を返す
            return middle
        elif data[middle] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = middle + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = middle - 1
    return -1            # 見つからなかった場合


# binary_search(list, search_value)
print(binary_search(list, search_value))
