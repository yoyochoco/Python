#2/24作業

#計算每人總分、平均
grades=[ ['A',68,74,64,81,0,0,0] , ['B',77,80,65,72,0,0,0] , ['C',95,90,82,85,0,0,0,] , ['D',42,55,45,48,0,0,0]]
for i in range(0,4):
    k = 0
    for j in range(1,5):
        k=k+grades[i][j]
    grades[i][5]=k
    grades[i][6]=k/4


#計算排名
m = []                                   #list m 紀錄 總分
for i in range(0,4):
    m.append(grades[i][5])

m.sort(reverse=True)                    #排序分數

for i in range(0,4):
    for j in range(0,4):
        if m[i] == grades[j][5]:
            grades[j][7] = i+1
            break

print(grades)