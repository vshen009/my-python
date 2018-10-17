while True:
	mode = input('请输入游戏选项:')
	if mode == 'q': #quit
		break
	elif mode == '1': #模式一
		print('启动模式1')
	elif mode == '2':
		print('启动模式2')
	else:
		print('只能输入 1/2/q')