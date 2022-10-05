
def spiralOrder(matrix):

    outt = []

    def once(matrix,start_i, start_j):
        if not matrix:
            return
        col = len(matrix[0])
        row = len(matrix)
        a = col
        b = row
        if col<=0 or row <= 0:
            print("是的")
            return
        i, j = start_i, start_j
        if i>=row or j>=col or i<0 or j<0:
            return
        while j < col:
            outt.append(matrix[i][j])
            j += 1
        j -= 1
        i += 1
        if i >= row or j >= col or i<0 or j<0:
            return
        while i < row:
            outt.append(matrix[i][j])
            i += 1
        i -= 1
        j -= 1
        if i >= row or j >= col or i<0 or j<0:
            return
        while j >= start_j:
            outt.append(matrix[i][j])
            j -= 1
        j += 1
        i -= 1
        if i >= row or j >= col or i<0 or j<0:
            return
        while i > start_i:
            outt.append(matrix[i][j])
            i -= 1
        matrix = matrix[1:-1]
        emp = []
        [emp.append(i[1:-1]) for i in matrix]
        matrix = emp

        once(matrix, 0, 0)


    once(matrix, 0, 0)

    return outt
# cc=[[7],[9],[6]]
# out = spiralOrder(cc)
# print(out)

test1 = [1,2,3]
test2 = [4,5,6]

cc = list(zip(test1,test2))
print(cc) #[(1, 4), (2, 5), (3, 6)]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("好好")
print(*matrix)
print(zip(matrix))
ccc = zip(*matrix)
print(ccc)
print("好")
print(list(zip(*matrix))[::-1])  #*matrix拆开二维矩阵

yy = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
dd = list(zip(*yy))  #转置整体所有元素取反是逆时针转90度 转置每一行分别取反是顺时针转90
print(dd)

matrix = [(1,2,3),(4,5,6),(7,8,9)]
pp = [1]
print(type(pp))
# print(matrix.pop(0))
# print(type(matrix.pop(0) ))
pp.extend((matrix[0]))     #这种加法固定加的是整体的拆包
# pp[0] = matrix.pop(0)
print(pp)
d = [0]*10
print(d)


c = [1,2,3,4,5]
d = [1,2,3,4,5,6]
if c not in d:
    print("erroe")

a = [1,2,3]
b = [5,6,7]
cccc = zip(a,b)
print(*cccc)

