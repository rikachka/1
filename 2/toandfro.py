width = int(input())
str = raw_input()
heigth = len(str) // width
str_list = [x for x in str]
order = 1
column = line = i = 0
while line < heigth:
	while column < width and column >= 0:
		str_list[line + column*heigth] = str[i]
		i = i + 1
		column = column + order
	order = 0 - order
	column = column + order
	line = line + 1
new_str = ''.join(str_list)
print(new_str)
