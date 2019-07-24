import time
import random
print("\x1B[32m")
for i in range(100):
	s = ''
	for j in range(30):
		s += str(random.randint(0,9)) + ' '
	print(s)
	time.sleep(0.1)
print("\x1B[0m")
