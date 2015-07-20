hodorian_cycle = ['h', 'o', 'd', 'o', 'r'] 

def hodor_word(word):

	new_word = ''
	for index in range(0,len(word)):
		hodex = index % 5
		new_word = new_word + hodorian_cycle[hodex]
	print(new_word)



dictum = input("Enter text to be dictated by his Hodorliness: ")

words = str.split(dictum)
hodorlyDecree = []

for word in words:
	hodor_word(word)

"""for word in words:
	print(word)
	tempword = ''
	if word[0].isupper():
		tempword = tempword + 'H'
	print(tempword)
"""