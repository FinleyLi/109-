import myClass as mc
from myClass import multi
import whatIsMyIp as ip

def minus(num1, num2):
	minu = num1 - num2
	return minu

def main():
	print(mc.adder(3, 5))
	print(f'multi: {multi(20, 30)}')
	print('minus: ', minus(51, 1))
	ip.main()

if __name__ == '__main__' :
	main()