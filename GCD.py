def gcd(a,b):
	a1 = a if a > b else b
	b1 = b if a > b else a
	r = -1
	while r != 0 :
		r = a1%b1
		a1 = b1
		b1=r
	return a1

if __name__ =='__main__':
    print(gcd(74381920,3421))
