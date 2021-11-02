import random
from tkinter.constants import X
n=random.randint(1,1000)
m = 0
while True:
	ans=int(input('enter your guess:'))
	if ans== n:
		print('success! you win! with' + str(m) + 'guesses!' )
		import random
		n=random.randint(1,1000)
	elif ans==0:
		print('goodbye')
		break
	elif ans>n:
		print('too high.')
		m=m+1
	else:
		print('too low.')
		m=m+1
	
