#print的格式化輸出

#format練習
test = ["123",'456',3]
print("測試：{} 測試2：{}".format(test[0],test[1]))
print()

print('測試{} 測試{}'.format('hi','你好'))
print()

print('測試{} 測試{}'.format(test[2],test[0]))
print()

print('測試{1} 測試{0}'.format('hi','world'))
print()

print('{} {}'.format('測試1','測試2'))
print()

print('測試1{0:3d}  測試2{1:.2f}'.format(12,3.4567))
print()

#%練習
a = 2
b = 1.2345
print('%2d %0.3f'%(a,b))
print()

print('%2d %0.5f'%(15,1.23456789))
print()