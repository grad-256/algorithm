# マージソート

list_a = [5, 7, 6, 4, 5, 1, 2, 3, 2, 2, 9, 1, 4]


def merge_sort(arr):
    if len(arr) > 1:
        res = []  # 返り値の配列
        mid = len(arr) // 2  # 配列のまん中の値
        L = arr[:mid]  # [1,2,3,4] => [1,2]
        R = arr[mid:]  # [1,2,3,4] => [3,4]
        L = merge_sort(L)
        # [4,1,3,2]
        # L: 4,1, R: 3, 2 (merge_sort: 1回目)
        # merge_sort(L(4,1)), merge_sort(R(3,2)) (merge_sort: 1回目)
        # L: 4, R:1     L: 3, R: 2 (merge_sort(2回目))
        # merge_sort(L(4)), merge_sort(R(1))      merge_sort(L(3)), merge_sort(R(2)) (merge_sort(2回目))
        # 4,1    3,2(merge_sort(3回目))
        # 4, 1 => 1,4  3,2 => 2,3(merge_sort(2回目))
        # L(1,4) R(3,2) =>  1,2,3,4 (merge_sort(1回目))
        # 4,1,3,2 => 1,2,3,4

        R = merge_sort(R)  # [2] => 2
        i = j = 0  # iはLを探索するインデックス, jはRを探索するインデックス
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            elif L[i] > R[j]:
                res.append(R[j])
                j += 1
            else:
                res.append(L[i])
                i += 1
        while i < len(L):
            res.append(L[i])
            i += 1
        while j < len(R):
            res.append(R[j])
            j += 1
        return res
    else:
        return arr


print(merge_sort(list_a))


def merge_sort02(data):
    if len(data) <= 1:
        return data

    # 分割操作
    mid = len(data)//2  # 真ん中を計算
    left = merge_sort02(data[:mid])  # 再帰で前半を分割してleftに
    right = merge_sort02(data[mid:])  # 再帰で後半を分割してrightに

    merge, l, r = [], 0, 0  # mergeに統合

    # 統合操作
    while l < len(left) and r < len(right):  # leftとrightの両方に要素がある場合
        if left[l] <= right[r]:  # 左側<=右側の場合
            merge.append(left[l])  # 左側をmergeに加える
            l += 1
        else:  # 左側>右側
            merge.append(right[r])  # 右側をmergeに加える
            r += 1
    if l < len(left):  # 左側が余った場合に残りを追加
        merge.extend(left[l:])  # extend 末尾に別のリストやタプルを結合
    elif r < len(right):  # 右側が余った場合に残りを追加
        merge.extend(right[r:])
    return merge


print(merge_sort02(list_a))
