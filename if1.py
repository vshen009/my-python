#大于20岁可以投票判断程序

age = input('请输入年纪:')
age = int(age)

if age < 13:
	print('你不可以投票,国小生')
elif age >=13 and age < 18:
	print('你不可以投票,国高中生')
elif age >=18 and age < 20:
	print('你不可以投票,大学生')
else:
	print('你可以投票了,社会人')