import random
r = random.randint(1,100)
while True:
	w = input('請輸入要猜的數字~ ')
	w = int(w)
	if w == r:
		print('你猜對了耶！數字正好就是',w,'你真是太厲害了~')
		break
	elif w < r:
		print('不對喔~比數字小!請再試試看!')
	elif w > r:
		print('不對喔!比數字大!請再試試看!')
