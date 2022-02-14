# 選択ソート 最小値（最大値）を選んで並び替えて整列させる

list_a = [3,4,5,6,6,7,1,4]

# i: 0 => list_aの長さ-1までループしたインデックス
for i in range(len(list_a)):
    # min_idx: i以上のインデックスでlist_aに最小値の入っているインデックス
    min_idx = i
    # j: i+1 => list_aの長さ-1
    for j in range(i+1, len(list_a)):
        if list_a[min_idx]>list_a[j]:
            min_idx = j
    list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]

print(list_a)
