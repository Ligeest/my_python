for number in range(1,10):
    print(number)
#只输出1~9
n = list(range(1,5))
print(n)
n1 = list(range(2,12,2))
#2~11内从2开始每次加2
print(n1)
print(str(min(n1))+"\n"+str(max(n1))+"\n"+str(sum(n1)))
#列表解析
n2 = [a**2 for a in range(1,10)]
#for结尾没有冒号
print(n2)