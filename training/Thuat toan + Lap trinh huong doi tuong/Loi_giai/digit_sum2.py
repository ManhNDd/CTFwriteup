#coding: utf-8


import sys
from decimal import *

getcontext().prec = 1000

if (sys.version_info[0] == 3):
	raw_input = input

def nDiv2(n):
	'''
	return number of even numbers of interval [0, n]
	'''
	if (n % 2 == 1): return nDiv2(n-1)
	return Decimal(n)/2+1

mDict = {} # remember the results of digitSum
def digitSum(n):
	'''
	recursion with memoization
	return digit sum of even numbers of interval [0, n]
	Formular for a four-digit number abcd:
	digitSum(abcd) = a*(a-1)/2*nDiv2(999) + a*digitSum(999) + a*nDiv2(bcd) + digitSum(bcd)

	Note: python 3 uses float
	'''
	if n in mDict: return mDict[n]
	strN = str(n)
	if len(strN) < 2:
		if (n % 2 == 1): n = n-1
		return n*nDiv2(n)/2
	tmp999 = Decimal(10**(len(strN)-1)) - 1
	a = Decimal(strN[0])
	bcd = Decimal(strN[1:])
	ret = a*(a-1)/2*nDiv2(tmp999) + a*digitSum(tmp999) + a*nDiv2(bcd) + digitSum(bcd)
	mDict[n] = ret
	return ret

def main():
	T = raw_input().strip()
	T = int(T)
	for i in range(T):
		N1, N2 = raw_input().strip().split(' ')
		N1 = Decimal(N1)
		N2 = Decimal(N2)
		if (N1 == 0): r = digitSum(N2)
		else: r = digitSum(N2) - digitSum(N1-1)
		print(int(r))

main()
