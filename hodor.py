from textstat.textstat import textstat

hodorian_syllables = ['Ho', 'dor']
hodorian_cycle = ['h','o','d','o','r']
hodorly_decree = ''

#takes in a word, returns the hodorically-correct hodor syllables
def hodorify_syllables(word):

  new_word = ''

  #count syllables in each word
  syl_count = int(textstat.syllable_count(word))

  for index in range(0,syl_count):

    hodex = index % 2

    if not word[index].isalpha():
      new_word += word[index]

    elif word[index].isupper():
      new_word += hodorian_syllables[hodex]

    else:
      new_word += hodorian_syllables[hodex].lower()

  return(new_word)

#takes in a word, returns the hodorically-correct hodor
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

dictum = str.split(raw_input("\nEnter text to be dictated by his Hodorliness: \n"))

for word in dictum:
  hodorly_decree += hodorify_syllables(word) + ' '

print('\nHodorly Decree: \n' + str(hodorly_decree))
