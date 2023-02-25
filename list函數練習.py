#list操作

#原始題目設定
name = ['Bob','Sam','Johnny','Tom','Frank']
print(name)
print()

#append使用
name.append('Mario')
print(name)
print()

name.append(['Job','Kitty'])
print(name)
print()

#extend使用
name.extend('Tommy')            #Tommy的每個字元都被分開來存取
print(name)
print()

name.extend(['Lux','Tim'])
print(name)
print()

#remove的使用
name.remove('Mario')
print(name)
print()
