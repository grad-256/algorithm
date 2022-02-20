# ジェネレータ関数
import sys


def generator(max):
    print('ジェネレータ作成')
    for n in range(max):  # n=>0
        try:
            x = yield n
            print('x = {}'.format(x))
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')


# gen = generator(10)
# next(gen)
# gen.send(100)
# gen.throw(ValueError('Invalid Value'))
# gen.close()
# next(gen)
# for x in gen:
#     print('x = {}'.format(x))
# send

# サブジェネレータ

def sub_sub_generator():
    yield "Sub Subのyield"
    return "sub sub のreturn"


def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "subのreturn"


def generator():
    yield "generatorのyield"
    res = yield from sub_generator()
    print('gen res = {}'.format(res))
    return 'generatorのreturn'


gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# list, generator memory


list_a = [i for i in range(100000)]


def num(max):
    i = 0
    while i < max:
        yield i
        i += 1

# for i in num(100000):
#     print(i)


gen = num(100000)
# print(sys.getsizeof(list_a))
# print(sys.getsizeof(gen))

# if 1行 lambda

y = 10
x = 0 if (y-20) > 0 else 1  # y>0 => 0 else 1
# print(x)


# def lambda_a(x): return x * x  # 引数x 返り値x*x
def lambda_a(x): return x * x

# print(lambda_a(10))


def lambda_b(x, y, z=5): return x * y * z


# print(lambda_b(2, 3))  # x=2, y=3, z=5 => 30
# print(lambda_b(2, 3, 4))  # x=2, y=3, z=4 => 24

# 条件式付きlambda


def lambda_c(x, y): return y if x < y else x  # if(x<y) => y, else x

# def lambda_c(x, y): return y if x < y else x  # if(x<y) => y, else x


# print(lambda_c(6, 4))

# リスト内包表記

list_a = (1, 2, 3, 'a', 4, 'b')  # タプル

list_b = [x*2 for x in list_a if type(x) == int]  # list_aのリスト
# print(list_b)
list_c = [x for x in range(100) if x % 7 == 0]
# print(list_c)


dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str]
# print(list_c)
list_a = tuple(x for x in range(100))
# print(type(list_a))


def func(n):
    for x in range(2, n):
        if n % x == 0:
            return True
    return False


list_a = [func(x) for x in range(100) if func(x) == False]
# print(list_a)

squarea = [n**2 for n in range(1, 6) if n % 2 == 1]
print(squarea)


A = [1, 2, 3]
B = [1, 2, 3]
C = [1, 2, 3]


def f():
    if not A:
        pass
    else:
        C.append(A.pop())
        f()
        B.append(C.pop())
        print('C = {}'.format(C))
        print('B = {}'.format(B))
        # print('B = {}'.format(B))


f()
