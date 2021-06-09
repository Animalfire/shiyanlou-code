for a in range (1,101):
	if 0 == (a%7) or 7 == (a//10) or 7 ==(a%10):
		continue
	else:
		print(a)