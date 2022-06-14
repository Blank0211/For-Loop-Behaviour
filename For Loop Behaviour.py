msg1 = 'a e i o u'.split()
vowels = 'aeiou'
loop_num = 1
index_position = 0

print('We\'ll use a For Loop to filter out vowels from a "List" of characters:')
print(msg1)
print('Since every character in the List is a vowel,\
 the List should be empty by the end of the For Loop.')
print()


for l in msg1:
	enum_msg1 = list(enumerate(msg1))
	
	for x,y in enum_msg1:
		print('Index {}: {}'.format(x, y), end='.     ')
	
	print('\nThis is loop number {}'.format(loop_num))
	
	print('The variable l is at index_position {0}'.format(index_position))
	
	# This is a For Loop to filter out vowels
	if l in vowels:
		print('{} will be removed'.format(l))
		msg1.remove(l)

	print('\n')
	
	loop_num += 1
	index_position += 1

#Printing out the list after the For Loop
print('\n', msg1)



print('\nSince 2 is the last index, the For Loop ends.')
print('As you can see from the results; the for loop iterates upon each index sequentially\
\nthis results in some of the vowels being left out ')
