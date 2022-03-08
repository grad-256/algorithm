# ヒープソート（昇順）※ヒープ領域とは無関係
# リストの並び替えを二分ヒープ木を用いて行うソートアルゴリズム
# 1,配列データをルートから順に左下からノードを作りそのノードから枝を作っていくように、作っていきながら順にソートしていく。大きいが数がルートに来るようにする
# 2,配列の値をツリーに入れ終わったら、戻していく。
# 1を繰り返す
# ヒープとは データ構造の一種 木構造のうち親要素が子要素より常に大きいとゆう条件を満たす
# 木構造の、要素部分を節（ノード node）、子のない末端の節を葉（リーフ leaf）、
# 親のない先頭の節を根（ルート root）といいます。要素と要素のつながりは、枝（ブランチbranch）です。
# ある節とその下の部分を取り出すと、それだけでも木構造となっています。これを部分木といいます。
import random


def max_heapify(array, n, i):
    """
    array : 対象とする配列
    n : heapifyの対象とする最後のインデックス
    i : subtree の root のインデックス
    """
    # ルート array[i]
    # とりあえずルートが最大
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 左側の子がルートより大きい場合
    if left < n and array[i] < array[left]:
        largest = left

    # 右側の子がルートよりも左側よりも大きい場合
    if right < n and array[largest] < array[right]:
        largest = right

    # ルート以外がルートより大きい場合は入れ替え
    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        # 入れ替えのあったsubtreeでmax-heapを満たすようにheapifyを行う
        max_heapify(array, n, largest)


def heap_sort(array):
    n = len(array)
    # max-heapを作る
    for i in range(n//2, -1, -1):
        max_heapify(array, n, i)

    # 配列の最初の最大値と配列の最後と交換する。
    # 配列の最後を除いた配列で、再びmax-heapを作る。
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heapify(array, i, 0)


if __name__ == '__main__':
    # 乱数シードを設定し毎回同じ乱数を出す
    random.seed(1)
    # 1000までの数で10個の値のある配列を生成する
    array = [random.randrange(1000) for i in range(10)]
    print('未ソート', array)  # 未ソート [17, 72, 97, 8, 32, 15, 63, 97, 57, 60]
    heap_sort(array)
    print('ソート済み', array)  # ソート済み [8, 15, 17, 32, 57, 60, 63, 72, 97, 97]
