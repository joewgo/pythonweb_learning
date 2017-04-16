try:
	age = int(input('請輸入年齡？'))
	if age >= 20:
		print('你已有投票權!!')
	else:
		print('你目前要等到20歲以上才有投票權，乖喔～。')
except ValueError:
	print('請輸入數字…謝謝')
else:
	pass
finally:
	pass