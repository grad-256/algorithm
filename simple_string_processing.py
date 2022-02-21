# 文字列処理 先頭から一文字づつパターンを比較して、不一致の文字が現れたら、比較するテキストの位置を一文字進める

def search(text, pattern):
    for i in range(len(text)):
        for j in range(len(pattern)):
            print(text[i+j])
            print(pattern[j])
            if text[i+j] == pattern[j]:
                if j == len(pattern) - 1:
                    return i
                else:
                    break
            else:
                break
    return -1


list = ["テ", "ス", "ト"]
data = search("ストテ", list)
print(data)
