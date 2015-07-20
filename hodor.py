hodorian_cycle = ['h', 'o', 'd', 'o', 'r']

def hodorify_word(word):

	new_word = ''

	for index in range(0,len(word)):
		
		hodex = index % 5

		if not word[index].isalpha():
			new_word += word[index]

		elif word[index].isupper():
			new_word += hodorian_cycle[hodex].upper()
			
		else:
			new_word += hodorian_cycle[hodex]

	return(new_word)

dictum = str.split(input("\nEnter text to be dictated by his Hodorliness: \n"))
hodorly_decree = ''

for word in dictum:
	hodorly_decree += hodorify_word(word) + ' '

print('\nHodorly Decree: \n' + str(hodorly_decree))