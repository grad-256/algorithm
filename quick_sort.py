# クイックソート 最も高速なソートアルゴリズム
# 基準値を設定し、基準値より大きい値を集めた部分列と小さな値を集めた部分列に振り分けて、この部分列で再帰を行いそれらを繰り返す

def quick_sort(data):
    n = len(data)
    pivot = data[n//2]  # 今回の基準値には、真ん中の値を利用
    left, right, middle = [], [], []
    for i in range(n):  # 分割処理 パーテーション
        if data[i] < pivot:  # 基準値より小さい場合は、左部分列leftに追加
            left.append(data[i])
        elif data[i] > pivot:  # 基準値より大きい場合は、右部分列rightに追加
            right.append(data[i])
        else:
            middle.append(data[i])  # 基準値と同じ場合には、部分列middleに追加
    if left:
        left = quick_sort(left)  # 再帰でleftを分割
    if right:
        right = quick_sort(right)  # 再帰でrightを分割
    return left + middle + right  # 順番に部分列を結合させて、戻り値にする


list_a = [5, 7, 6, 4, 5, 1, 2, 3, 2, 2, 9, 1, 4]
afterdata = quick_sort(list_a)
print(afterdata)
