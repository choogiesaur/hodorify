hodorian_cycle = ['h', 'o', 'd', 'o', 'r']

def hodorify_word(word):

	new_word = ''

	for index in range(0,len(word)):
		
		hodex = index % 5

		if word[index].isupper():
			new_word += hodorian_cycle[hodex].upper()
		else:
			new_word += hodorian_cycle[hodex]

	print(new_word)

dictum = input("Enter text to be dictated by his Hodorliness: ")

words = str.split(dictum)
hodorlyDecree = []

for word in words:
	hodorify_word(word)