# ハッシュ法

class HashTable(object):
    def __init__(self):
        self.size = 12  # 配列のサイズ
        self.keys = [None] * self.size  # キーの配列
        self.values = [None] * self.size  # 値の配列

    def make_hash(self, key):
        hash_val = 0
        for pos in range(len(key)):
            hash_val += ord(key[pos])  # ord 文字をUnicode値に変換する関数

        hash_val %= self.size
        return hash_val

    # 線形走査法
    # 次のインデックスが空かどうかを調べ、余りを取ることでインデックスが配列サイズを超えたら0に戻って調べる
    def add(self, key, data):
        index = self.make_hash(key)
        print(index)
        # 空のインデックスを探し、もし同じキーが存在したら値を更新
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            # 次のインデックスに進みサイズを超えたら最初に戻る
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = data

    def lookup(self, key):
        index = self.make_hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return False


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('apple', 10)
    # hash_table.add('banana', 5)
    # hash_table.add('orange', 20)
    # [None, None, 'apple', None, 'banana', None, None, None, None, 'orange', None]
    print(hash_table.keys)
    # [None, None, 10, None, 5, None, None, None, None, 20, None]
    # print(hash_table.values)
    # 10
    # print(hash_table.lookup('apple'))
