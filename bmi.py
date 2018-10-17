while True:
    wegiht = input('请输入你的体重 KG: ')
    hight = input('请输入你的身高 CM: ')
    if wegiht.isdigit() == True and hight.isdigit() == True:
        wegiht = float(wegiht)
        hight = float(hight)/ 100
        bmi = wegiht / (hight * hight)
        print('你的BMI值是: ', bmi)
        if bmi <= 18.5:
            print('你的体型偏瘦,多吃点')
        elif bmi > 18.5 and bmi < 24.9:
            print('你的体型正常,请保持')
        elif bmi >= 25 and bmi < 29.9:
            print('你的体型肥胖,请减肥')
        elif bmi >= 30 and bmi < 34.9:
            print('如果你摔倒了大概会引发2级地震,参加魔鬼训练营吧.')
        else:
            print('这,我们还是聊聊地球和平的问题吧.')
        break
    elif wegiht == 'q' or  hight == 'q':
        break
    else:
        print('请输入正确得身高和体重,必须是数字,或者按q退出')
