#打包
CCE_n = ['一年級','二年級','三年級','四年級','碩士班']
CCE_s = [102,98,100,87,25]
CCE = []
CCE_count = []
for p in zip(CCE_n,CCE_s):
    CCE.append(p)
    print(p)
print(CCE)
print()

for q in enumerate(CCE):
    CCE_count.append(q)
    print(q)
print(CCE_count)