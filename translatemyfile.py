from queue import PriorityQueue
from translate import Translator

translator= Translator(to_lang="ja")

with open("./jap.txt") as my_file:
	text = my_file.read()
	translation = translator.translate(text)
	print(translation)