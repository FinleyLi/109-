import myClass as mc
from myClass import multi
import whatIsMyIp as ip
import inspect

def minus(num1, num2):
	minued = num1 - num2
	return minued

def main():
	'''
	print(mc.adder(3, 5))
	print(f'multi: {multi(20, 30)}')
	print('minus: ', minus(51, 1))
	ip.main()
	'''
	print(inspect.getsource(mc.adder))

if __name__ == '__main__' :
	main()