a = [5, 1, 3, 4]
b = ["あ", "い", "う", "え"]

print(a)
print(b)

print(a[0])

print(a[2])


print("能")

c = 5
a = [c, 1, 3, 4]
print(a)

a = [1] * 4
print(a)

#空のリスト
e = list()

n = list(range(5))
print(n)  #->[0,1,2,3,4] 0から5未満

s = list("abcde")
print(s)
s = ["a", "b", "c", "d", "e"]
print(s)

t = "a textbox of Python"
tlist = t.split()
print(tlist)
tlist = "a textbox of python".split()
print(tlist)

#リストの要素へのアクセス
a = [5, 1, 3, 4]
print(a[0])

print(a)
a[1] =  2
print(a)

print(len(a)) #リストの数

#負の添え字
a = [5, 1, 3, 4]
print(a[-1]) #後ろから

#スライス
a = [5, 1, 3, 4]
b = a[1:3] #先頭番号：終了番号 文字と文字の間
print(b)

#リストへの追加、結合
#append
a = [5, 1, 3, 4]
a.append(2)
print(a)

#extend
a = [5, 1, 3, 4]
b = [2, 6]
a.extend(b)
print(a) #[5, 1, 3, 4, 2, 6]

a = [5, 1, 3, 4]
b = [2, 6]
a.append(b)
print(a) #[5, 1, 3, 4, [2, 6]]

#リストの代入と複製
a = [1, 2, 3]
b = a
print(a)
print(b)

b[0] = 0
a[1] = 0
print(a)
print(b)

a = [1, 2, 3]
b = a.copy()
b[0] = 0
a[1] = 0
print(a)
print(b)

#イミュータブルとミュータブル 変更不能（数値や文字列）と変更可能（リスト）
#イミュータブル
a = 1
b = a
b = 2
print(a, b)

a = 1
b = a
print(id(a), id(b))
b = 2
print(id(a), id(b))

#タプル
a = 1,2
print(a)
a = (1,2)
print(a)

(b, c) = a
b
1
c
2
print(b)
print(c)
print(a)
print(a[0])

#辞書
age = {"山田":18, "田中":19}
age
{'山田': 18, '田中': 19}

print(age)
print(age["山田"])

age["佐藤"] = 20
print(age)

print("岡田" in age)
print("佐藤" in age)

#for
for i in range(10):
  if i == 1:  #iが１なら次に移る
    continue
  if i== 8:  #iが８なら繰り返しから脱出
    break
  print(i)

#合計の計算
sum = 0  #合計を０に
for i in range(10):  #iは０から９
  sum = sum + i #sumにiを加える. sum += i
  print(sum)  #sumを表示

#for文の入れ子
for i in range(3):
  for j in range(3):
    print(i, j)

#リストの長さとrange関数
a = [5, 1, 3, 4]
for i in range(len(a)):
  print(i, a[i])

#リストをfor文で直接使う
a = [5, 1, 3, 4]
for d in a:
  print(a)

#enumerate関数
a = [5, 1, 3, 4]
for i, d in enumerate(a):
  print(i, d)

#リストの要素の平均値
a = [5, 1, 3, 4]
sum = 0
for i in range(len(a)):
  sum += a[i]
average = sum/len(a)
print(average)

#for文を使ったリストの内包表記
#[0, 1, 4, 9, 16] 値が添え字の２乗のリスト
a = []
for i in range(5):
  a.append(i*i)
print(a)

a = [i*i for i in range(5)]
print(a)
