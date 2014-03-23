#for i in range(1000):
#	if (i**3 - 888) % 1000 == 0:
#		print(i)
# These numbers: 192, 442, 692, 942

n = int(input())
i = 0


while i < n:
	k = input()
	first_part = (k-1) // 4
	k = k % 4
	if k ==1:
		second_part = 192
	elif k==2:
		second_part = 442
	elif k==3:
		second_part = 692
	elif k==0:
		second_part = 942
	answer = first_part*1000 + second_part
	print(answer)
	i = i + 1
