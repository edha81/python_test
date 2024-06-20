#LIST 列表
''' 
a = [0,1,2,3]
b = [4,3,2,1]

a.extend(b)  a後面延伸b
print(a)
0,1,2,3,4,3,2,1

a.append(10) a新增10
print(a)
0,1,2,3,10

a.insert(2,30) 在第3個位置插入30
print(a)
0,1,30,2,3

a.remove(0) 把0的值刪掉

a.clear() 清空

a.pop() 移除最後一位

a.sort() 小到大排序

a.reverse()  反轉列表

print(a.index(0)) 回傳該值第一個位置 
0

print(a.count(0)) 該值總數
1
'''
#元組 TUPLE 跟LIST差別在裡面資料不能變更 ex: a = (0,1,2)

def max(a,b):
    if a > b:
        print('max = a')
    elif a < b:
        print('max = b')
    else:
        print('same')

max(2,2)