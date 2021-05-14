# вывод символов в порядке убывания

textfile = open('text.txt', 'r')
array = [text for text in textfile]
strings = ''.join(array)
lowletter = [s.lower() for s in strings if s.isalpha()]
text_letters = list(set(lowletter))
sort_key = lambda s: lowletter.count(s)
text_letters.sort(key=sort_key, reverse=True)
for letter in text_letters:
    print(letter, lowletter.count(letter))
textfile.close()
