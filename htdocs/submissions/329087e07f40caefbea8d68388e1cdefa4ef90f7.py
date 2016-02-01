def seven_seg(input):
	table = [
		[' _ ','   ',' _ ',' _ ','   ',' _ ',' _ ',' _ ',' _ ',' _ '],
		['| |','  |',' _|',' _|','|_|','|_ ','|_ ','  |','|_|','|_|'],
		['|_|','  |','|_ ',' _|','  |',' _|','|_|','  |','|_|',' _|']]

	result = ''

	for i in[0, 1, 2]:
		for j in input:
			result += table[i][int(j)]

		result += '\n'

	return result
