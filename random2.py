import random
r = random.randint(1,100)
runtime =0 
while True:
   num = int(input('请输入一个整数比大小:'))
   runtime = runtime + 1
   if num == r:
        print('恭喜你猜对了,正确数字是:' , r)
        print('   这是第', runtime ,'次猜测')
        break
   elif num > r:
        print('   你输入的数字大了')
        print('   这是第', runtime ,'次猜测')
   elif num < r:
        print('   你输入的数字小了')
        print('   这是第', runtime ,'次猜测')


    