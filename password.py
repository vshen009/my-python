#密码重置 三次倒计时
i = 0 #设置密码输入倒计时
time = 2 #密码输入的机会
while i < 3 :
    password = input('请输入密码:')
    if password == 'a123456':
        print('恭喜,登陆成功')
        break
    elif time > 0 :
        print('密码错误~! 还有', time , ' 次机会!')
        time = time - 1
    i = i + 1
