from textstat.textstat import textstat

hodorian_syllables = ['Ho', 'do', 'r']
hodorian_cycle = ['h','o','d','o','r']
hodorly_decree = ''

#takes in a word, returns the hodorically-correct hodor syllables
def hodorify_syllables(word):

  new_word = ''
  index = 0

  #count syllables in each word
  syl_count = int(textstat.syllable_count(word))

  #get initial and final punctuation
  word_start = 0
  for word_start in range(0,len(word)):
    if word[word_start].isalpha():
      break

  word_end = len(word)
  for word_end in range(len(word),1,-1):
    if word[word_end-1].isalpha():
      break  

  #split word from punctutation
  pre_text = word[:word_start]
  post_text = word[word_end:]
  word = word[word_start:word_end]

  #for each syllable of the word, print a ho-dor syllable
  for syl_index in range(0,syl_count):

    hodex = syl_index % (len(hodorian_syllables)-1)
    dordex = 0

    for dordex in range(0,len(hodorian_syllables[0])):
      if word[index+dordex].isupper():
        new_word += hodorian_syllables[hodex][dordex].upper()

      else:
        new_word += hodorian_syllables[hodex][dordex].lower()
      
    index += len(hodorian_syllables[0])

  #only print the final r at the end of the word
  if hodex == 1:
    if word[index].isupper():
      new_word += hodorian_syllables[2].upper()
    else:
      new_word += hodorian_syllables[2]
  return(pre_text+new_word+post_text)

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
