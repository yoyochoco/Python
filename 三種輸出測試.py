#格式化輸出練習
x = '測試x'
y = '測試y'
z = '測試z'
a = 10
b = 15.00
c = 200000

#舊版%
print('%s and %2d'%(x,a))
print()

#測試新版format()
print('{:2d} and {:^10}'.format(a,y))
print()

#測試最新版f-string
print(f'{x:>10} and {a:3d}')