'''
import time
def get(number):
    list1 = [1,1]
    a = 1
    b = 1
    for i in range(number-2):
        r = a+b
        #list1.append(r)
        a = b
        b = r
    return(str(r))

time1 = time.time()
with open('number.txt',mode='w')as f:
    f.write(get(1000000))
#print(get(20))
time2 = time.time()
print(time2-time1)
'''
with open('number.txt',mode='r')as f:
    print(len(f.read()))

