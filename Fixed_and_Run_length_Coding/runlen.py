#Run Length Encoding Function
def runlen(st):
	n = len(st)
	i = 0
	new_st = ""
	while i < n- 1:
		cnt = 1
		while (i < n - 1 and st[i] == st[i + 1]):
			cnt += 1
			i += 1
		i += 1

		new_st += (st[i - 1] + str(cnt))
	return new_st

#main code
if __name__ == "__main__":
	fhand = open('input.txt')
	st = fhand.read()       
	new_st = runlen(st)

	print('Run length Encoded String:-')
	print(new_st)
	print( '\nLength in bytes before compression:- '+ str(len(st)))
	print( 'Length in bytes after compression:- ' + str(len(new_st)))
	print( 'Compression ratio:- ' + str(float(len(st))/len(new_st)))